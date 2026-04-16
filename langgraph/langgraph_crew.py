from langgraph.graph import StateGraph, END
from langchain_ollama import OllamaLLM
from typing import TypedDict

# Endpoint 1 — Mistral til planlægning og dokumentation
llm_mistral = OllamaLLM(model="mistral:7b-instruct-q4_K_M", base_url="http://localhost:11434")

# Endpoint 2 — Llama3 til kodning og test
llm_llama = OllamaLLM(model="llama3:8b", base_url="http://localhost:11435")

class State(TypedDict):
    architecture: str
    tickets: str
    code: str
    tests: str
    readme: str
    deployment: str

def architect(state):
    print("\n[Architect] Designing API...")
    result = llm_mistral.invoke(
        "You are a software architect. Design a minimal Flask to-do list REST API. "
        "List the files needed and the endpoints. Be concise."
    )
    with open("architecture.md", "w") as f:
        f.write(result)
    return {"architecture": result}

def techlead(state):
    print("\n[Tech Lead] Writing tickets...")
    result = llm_mistral.invoke(
        f"You are a tech lead. Based on this architecture:\n{state['architecture']}\n"
        "Write 4 implementation tickets. Each needs a title, scope, and one-line definition of done. Be concise."
    )
    with open("tickets.md", "w") as f:
        f.write(result)
    return {"tickets": result}

def developer(state):
    print("\n[Developer] Writing code...")
    result = llm_llama.invoke(
        f"You are a Python developer. Based on this architecture:\n{state['architecture']}\n"
        "Write complete app.py for a Flask to-do list API with in-memory storage. "
        "Include GET, POST, PUT, DELETE for /tasks. Only output the code, no explanation."
    )
    with open("app.py", "w") as f:
        f.write(result)
    return {"code": result}

def tester(state):
    print("\n[QA Engineer] Writing tests...")
    result = llm_llama.invoke(
        f"You are a QA engineer. Based on this Flask API code:\n{state['code']}\n"
        "Write pytest tests for GET, POST, PUT, DELETE on /tasks. Only output the code, no explanation."
    )
    with open("test_app.py", "w") as f:
        f.write(result)
    return {"tests": result}

def documenter_readme(state):
    print("\n[Tech Writer] Writing README...")
    result = llm_mistral.invoke(
        "Write a short README.md for a Flask to-do list API. "
        "Include how to install, run, and a list of endpoints."
    )
    with open("README.md", "w") as f:
        f.write(result)
    return {"readme": result}

def documenter_deployment(state):
    print("\n[Tech Writer] Writing DEPLOYMENT...")
    result = llm_mistral.invoke(
        "Write a short DEPLOYMENT.md checklist for running a Flask API locally. "
        "Include environment setup, how to run it, and 3 things to change before production."
    )
    with open("DEPLOYMENT.md", "w") as f:
        f.write(result)
    return {"deployment": result}

# Byg grafen
graph = StateGraph(State)
graph.add_node("architect", architect)
graph.add_node("techlead", techlead)
graph.add_node("developer", developer)
graph.add_node("tester", tester)
graph.add_node("documenter_readme", documenter_readme)
graph.add_node("documenter_deployment", documenter_deployment)

graph.set_entry_point("architect")
graph.add_edge("architect", "techlead")
graph.add_edge("techlead", "developer")
graph.add_edge("developer", "tester")
graph.add_edge("tester", "documenter_readme")
graph.add_edge("documenter_readme", "documenter_deployment")
graph.add_edge("documenter_deployment", END)

app = graph.compile()

print("=== LangGraph Multi-Agent Workflow ===")
result = app.invoke({})
print("\n=== Done! Files written to disk. ===")