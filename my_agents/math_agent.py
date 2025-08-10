from agents import Agent,ModelSettings
from my_config.gemini_config import model
from my_data_type.my_data_type_schema import MyData
from my_tools.math_tool import add,sub,mul,div
from my_tools.user_data_tool import fetch_user_data,fetch_user_dat_by_id
from agents.agent import StopAtTools
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
from my_tools.get_age_tools import get_age
from instructions.dynamic_instruction import dynamic_instruction
from user_data_type.user_data import UserDataType
from guardrial_function.guardrial_input_function import guardrial_input_function
from guardrial_function.guardrial_output_function import guardrial_output_function

hotel_assistant=Agent(
    name="Hotel Customer Care Assistant",
    instructions="""
You are a helplfull Mehran Hotel customer care assistant your name is Akhter Riyaz.
- Mehran Hotel owner name is Kazim Jabri.
- Mehran Hotel Total rooms 191.
- 20 rooms for not availabe for public it is only for special guest.
""",
model=model,
input_guardrails=[guardrial_input_function],
output_guardrails=[guardrial_output_function]
)

# my_assistant=Agent[UserDataType](
#     name="assistant",
#     instructions=dynamic_instruction,
#     model=model,
#     tools=[get_age]    
# )

# math_agent=Agent(
#     name="math-agent",
#     instructions=f"""{RECOMMENDED_PROMPT_PREFIX}
#     you are a helpfull for math assistant
# """,
#     model=model,
#     handoff_description="This is a math teacher"
# )

# english_agent=Agent(
#     name="english-agent",
#     instructions=f"""{RECOMMENDED_PROMPT_PREFIX}
#     you are a helpfull for english assistant
# """,
#     model=model,
#     handoff_description="This is a english teacher"
# )

# my_assistant=Agent(
#     name="my-assistant",
#     instructions="you are a helfull assistant",
#     model=model,
#     handoffs=[math_agent,english_agent]
# )

# for ag in my_assistant.handoffs:
#     print(f"{ag.name}: {ag.instructions}")


# first_agent=Agent(name="math-agent",instructions="you are helpfull for math calculations",model=model,tools=[add,sub,mul,div],tool_use_behavior=StopAtTools(stop_at_tool_names=["add","mul"]),model_settings=ModelSettings(tool_choice="sub",parallel_tool_calls=False),reset_tool_choice=True)

# last_agent=Agent(name="english-agent",instructions="you are helpfull assistant",model=model,tools=[first_agent.as_tool(tool_name="first-agent",tool_description="This is a math assistant tool")])



