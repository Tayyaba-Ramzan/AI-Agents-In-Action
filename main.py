from agents import Runner,set_tracing_disabled
from my_agents.math_agent import agent

set_tracing_disabled(True)

res=Runner.run_sync(starting_agent=agent,input="mujhy user ka data id chihe is ki id 1,6,9 ho")

print(res.final_output)