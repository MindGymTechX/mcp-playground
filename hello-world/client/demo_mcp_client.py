import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent

from langchain_openai import ChatOpenAI  # Use LangChain's OpenAI-compatible chat model
from print_dict import print_dict, pretty_print
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ----------------- Define model_id, base_url for your LMStudio server ------------------------------
model_id = "openai_gpt-oss-20b"
local_url = "http://localhost:1234/v1"
remote_url = "http://192.168.68.122:1234/v1"
base_url = local_url
# --------------------------------------------------------------------------------------------------


async def main():
    # Instantiate the chat model pointing to your LMStudio local server
    llm = ChatOpenAI(
        model=model_id,  # or the model name your LMStudio serves
        openai_api_base=base_url,
        openai_api_key="EMPTY",  # LMStudio usually does not require a key; use "EMPTY" or ""
        temperature=0,
    )

    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": [str(BASE_DIR / "server" / "math_server.py")],
                "transport": "stdio",
            },
            "weather": {
                "url": "http://localhost:8000/mcp",
                "transport": "streamable_http",
            },
        }
    )
    tools = await client.get_tools()
    print("tools = ", tools)
    agent = create_agent(
        llm,
        tools,
        system_prompt="If the question can't be answered by the given tools, use your internal knowledge to answer this"
    )

    messages = {"messages": [{"role": "user", "content": "what's (3 + 5) x 12?"}]}
    math_response = await agent.ainvoke(messages)
    print("Math response:", math_response)
    pretty_print(math_response)
    print(math_response["messages"][-1].content)

    messages = {"messages": [{"role": "user", "content": "what is the weather in Bangalore?"}]}
    weather_response = await agent.ainvoke(messages)
    print("Weather response:", weather_response)
    pretty_print(weather_response)
    print(weather_response["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
