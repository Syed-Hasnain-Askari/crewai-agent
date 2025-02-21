from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI
import os

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "your-openai-api-key"

# Define an AI agent
researcher = Agent(
    role="AI Researcher",
    goal="Find the latest AI trends",
    backstory="You are an expert in artificial intelligence research and technology advancements.",
    llm=ChatOpenAI(model="gemini/gemini-1.5-flash"),
    verbose=True  # Show logs for debugging
)

# Define a task for the agent
ai_trends_task = Task(
    description="Research the latest AI trends and summarize them in 3 bullet points.",
    agent=researcher,
    expected_output="A list of 3 key AI trends in bullet points."
)

# Create a crew and assign the task
crew = Crew(
    agents=[researcher],
    tasks=[ai_trends_task]
)

# Run the crew
result = crew.kickoff()
print("🔹 AI Research Results:\n", result)
