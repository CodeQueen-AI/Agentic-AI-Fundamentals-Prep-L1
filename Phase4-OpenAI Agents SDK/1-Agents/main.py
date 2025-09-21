from agents import (Agent,Runner, AsyncOpenAI, OpenAIChatCompletionsModel, enable_verbose_stdout_logging)
from dotenv import load_dotenv
import os

load_dotenv()
enable_verbose_stdout_logging()

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client,
)

agent = Agent(name="Assistant", model=model)

result = Runner.run_sync(agent, "What is the capital of Pakistan?")

print(result.final_output)