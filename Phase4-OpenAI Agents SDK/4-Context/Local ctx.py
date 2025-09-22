from agents import Agent , Runner , function_tool , RunContextWrapper
from dataclasses import dataclass
from config import model
import asyncio

@dataclass
class UserInfo : 
    name : str
    uid : int
    
@function_tool
def fetch_user_age(wrapper: RunContextWrapper [UserInfo]) -> str:
    """Fetch the age of the user"""
    print("Fetch User Age Tool called with Name" , wrapper.context.name)
    return f"The User {wrapper.context.name} is 17 Years Old"

async def main():
    user_info = UserInfo("CodeQueen" , 943123)
    
    agent = Agent(
        name = 'User Assistant',
        tools = [fetch_user_age],
        model=model,
    )
    
    result = await Runner.run(
        agent, 'What is a Age of user',
        context= user_info,
    )
    
    print(result.final_output)
    
asyncio.run(main())
