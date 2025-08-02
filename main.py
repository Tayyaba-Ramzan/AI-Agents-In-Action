from agents import Runner,set_tracing_disabled
from my_agents.math_agent import agent

set_tracing_disabled(True)

res=Runner.run_sync(starting_agent=agent,input="mujhy user k name ki list dai do yaaaaaar. or is k sath in k username bhi dai do naaaaa or email bhi")

print(res.final_output)