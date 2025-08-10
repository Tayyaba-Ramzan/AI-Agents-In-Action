from agents import Runner,set_tracing_disabled,InputGuardrailTripwireTriggered,OutputGuardrailTripwireTriggered
from user_data_type.user_data import UserDataType
from my_agents.guardrial_agent import guardrial_agent
from my_agents.math_agent import hotel_assistant

set_tracing_disabled(True)

user1=UserDataType("Muhammmad Hassan",27,"Software Engineer")

try:
    res=Runner.run_sync(starting_agent=hotel_assistant,input="How many rooms availabe in Mehran Hotel?",context=user1)
    # print(res.last_agent)
    print(res.final_output)
except InputGuardrailTripwireTriggered as e:
    print(f"Trip Input Triggered------------> \n {e}")

except OutputGuardrailTripwireTriggered as e:
    print(f"Trip Output Triggered------------> \n {e}")