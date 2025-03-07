# Deep Research AI Agentic System

## Overview
This project implements a **Deep Research AI Agentic System** that automates online information retrieval and response drafting using multiple AI agents. It leverages **Tavily API** for web searches, **Google Gemini AI** for response generation, and **LangChain** for multi-agent orchestration.

## Features
- **Multi-Agent Architecture:** Utilizes separate agents for research and response drafting.
- **Web Search Integration:** Uses Tavily API to fetch real-time data.
- **LLM Processing:** Employs Google Gemini AI to structure responses.
- **Memory Management:** Utilizes LangChain's `ConversationBufferMemory` for tracking interactions.
- **Flexible & Scalable:** Easily adaptable to different domains and queries.

## Workflow
1. **User Query:** The system receives a query (e.g., "What is the capital of France? List some famous landmarks in Paris.").
2. **Research Agent Execution:**
   - Calls the Tavily API to search for relevant information.
   - Retrieves structured results from the web.
3. **Drafting Agent Execution:**
   - Processes the search results using Google Gemini AI.
   - Generates a well-structured response.
4. **Final Output:** The response is returned to the user.

## Tech Stack
- **Python** (Main programming language)
- **LangChain** (Agent orchestration & memory management)
- **Tavily API** (Web search capability)
- **Google Gemini AI (1.5-Flash)** (LLM-based text generation)
- **dotenv** (Environment variable management)

## Installation & Setup
### Prerequisites
Ensure you have **Python 3.8+** installed. Then, install dependencies:
```bash
pip install langchain langchain_google_genai tavily google-generativeai python-dotenv
```

### Environment Variables
Create a `.env` file in the root directory and add:
```
GOOGLE_API_KEY=your_google_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key
```

### Running the Project
Run the script with:
```bash
python main.py
```

## Code Structure
```
├── main.py            # Core implementation of the multi-agent system
├── .env               # Stores API keys (not to be shared)
└── README.md          # Documentation
```

## Example Usage
**Input:**
```
What is the capital of France? List some famous landmarks in Paris.
```
**Processing:**
- Research Agent fetches latest information.
- Drafting Agent processes data and generates structured output.

**Output:**
```
The capital of France is Paris. Some famous landmarks include the Eiffel Tower, Louvre Museum, and Notre-Dame Cathedral.
```

## Future Improvements
- Support for additional research sources.
- Enhanced response formatting with structured markdown.
- Integration with other AI models like OpenAI GPT-4.

