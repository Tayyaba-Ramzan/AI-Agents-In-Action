from agents import Runner,set_tracing_disabled
from my_agents.math_agent import my_assistant
from user_data_type.user_data import UserDataType

set_tracing_disabled(True)

user1=UserDataType("Muhammmad Hassan",27,"Software Engineer")

res=Runner.run_sync(starting_agent=my_assistant,input="what is the age of user?",context=user1)

# print(res.last_agent)
print(res.final_output)