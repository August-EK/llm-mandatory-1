from crewai import Agent, Task, Crew, LLM, Process

# Endpoint 1 — Mistral bruges til planlægning og dokumentation
llm_mistral = LLM(
    model="ollama/mistral:7b-instruct-q4_K_M",
    base_url="http://localhost:11434",
    timeout=120
)

# Endpoint 2 — Llama3 bruges til kodning og test
llm_llama = LLM(
    model="ollama/llama3:8b",
    base_url="http://localhost:11434",
    timeout=120
)

architect = Agent(
    role="Software Architect",
    goal="Design a minimal Flask REST API for a to-do list",
    backstory="You are an experienced software architect.",
    llm=llm_mistral,
    verbose=True,
    max_iter=2,
    max_retry_limit=1,
    respect_context_window=True
)

techlead = Agent(
    role="Tech Lead",
    goal="Break the architecture into clear implementation tickets",
    backstory="You are a tech lead who writes clear task breakdowns.",
    llm=llm_mistral,
    verbose=True,
    max_iter=2,
    max_retry_limit=1,
    respect_context_window=True
)

developer = Agent(
    role="Python Developer",
    goal="Write complete working Python code for the Flask API",
    backstory="You are a Python developer who writes clean code.",
    llm=llm_llama,
    verbose=True,
    max_iter=2,
    max_retry_limit=1,
    respect_context_window=True
)

tester = Agent(
    role="QA Engineer",
    goal="Write pytest tests for the Flask API",
    backstory="You write thorough tests for Python APIs.",
    llm=llm_llama,
    verbose=True,
    max_iter=2,
    max_retry_limit=1,
    respect_context_window=True
)

documenter = Agent(
    role="Technical Writer",
    goal="Write developer documentation for the Flask API",
    backstory="You write clear and concise technical documentation.",
    llm=llm_mistral,
    verbose=True,
    max_iter=2,
    max_retry_limit=1,
    respect_context_window=True
)

task1 = Task(
    description="Design a minimal Flask to-do list REST API. List the files needed and the endpoints. Be concise.",
    expected_output="A short component overview and list of API endpoints.",
    agent=architect,
    output_file="architecture.md"
)

task2 = Task(
    description="Based on the architecture, write 4 implementation tickets. Each ticket needs a title, scope, and one-line definition of done. Be concise.",
    expected_output="4 short implementation tickets.",
    agent=techlead,
    output_file="tickets.md"
)

task3 = Task(
    description="Write app.py for a Flask to-do list API with in-memory storage. Include GET, POST, PUT, DELETE for /tasks. Only output the code, no explanation.",
    expected_output="Complete app.py code.",
    agent=developer,
    output_file="app.py"
)

task4 = Task(
    description="Write test_app.py with pytest tests for a Flask API with GET, POST, PUT, DELETE on /tasks. Only output the code, no explanation.",
    expected_output="Complete test_app.py code.",
    agent=tester,
    output_file="test_app.py"
)

task5 = Task(
    description="Write a short README.md for a Flask to-do list API. Include how to install, run, and a list of endpoints.",
    expected_output="Complete README.md",
    agent=documenter,
    output_file="README.md"
)

task6 = Task(
    description="Write a short DEPLOYMENT.md checklist for running a Flask API locally. Include environment setup, how to run it, and 3 things to change before production.",
    expected_output="Complete DEPLOYMENT.md",
    agent=documenter,
    output_file="DEPLOYMENT.md"
)

crew = Crew(
    agents=[architect, techlead, developer, tester, documenter],
    tasks=[task1, task2, task3, task4, task5, task6],
    verbose=True,
    process=Process.sequential
)

result = crew.kickoff()
print(result)