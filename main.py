import os
from tavily import TavilyClient
from langchain.agents import AgentType, initialize_agent
from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import Tool
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_GENERATIVE_AI_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize Tavily API
client = TavilyClient(os.getenv("TAVILY_API_KEY"))

def tavily_search(query: str):
    response = client.search(
        query=query,
        search_depth="advanced",
        max_results=2,
        time_range="day",
        include_answer="advanced"
    )
    return response

# Initialize LLM (replace with your preferred model)
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temperature=0.5,
              # create your google gemini api and store in .env file with variable GOOGLE_API_KEY
                           google_api_key=os.getenv("GOOGLE_API_KEY"))

def generate_response(prompt):
    try:
        response = model.generate_content(f"User query: {prompt}")
        return response.text
    except Exception as e:
        print(f"Error in generating response: {e}")
        return "Error generating response."


# Define tools
search_tool = Tool(
    name="Web Search",
    func=tavily_search,
    description="Search the web for relevant information using Tavily API."
)

drafting_tool = Tool(
    name="Answer Drafting",
    func=generate_response,
    description="Generate a structured response based on research data."
)

# Define memory
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Define the Research Agent
research_agent = initialize_agent(
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    tools=[search_tool],
    llm=llm,
    memory=memory,
    verbose=True
)

# Define the Answer Drafting Agent
answer_agent = initialize_agent(
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    tools=[drafting_tool],
    llm=llm,
    memory=memory,
    verbose=True
)

# Multi-Agent Workflow
# Multi-Agent Workflow
query = "What is the capital of France? List some famous landmarks in Paris."
search_results = research_agent.run(query)
final_answer = answer_agent.run(query + str(search_results))

print("Final Answer:", final_answer)
