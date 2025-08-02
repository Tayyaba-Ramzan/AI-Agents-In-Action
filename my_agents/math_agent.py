from agents import Agent
from my_config.gemini_config import model
from my_data_type.my_data_type_schema import MyData
from my_tools.math_tool import add,sub,mul,div
from my_tools.user_data_tool import fetch_user_data,fetch_user_dat_by_id


first_agent=Agent(name="math-agent",instructions="you are helpfull for math calculations",model=model,tools=[add,sub,mul,div])

last_agent=Agent(name="english-agent",instructions="you are helpfull assistant",model=model,tools=[first_agent.as_tool(tool_name="first-agent",tool_description="This is a math assistant tool")])



