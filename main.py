from agents import Runner,set_tracing_disabled
from my_agents.math_agent import first_agent,last_agent

set_tracing_disabled(True)

res=Runner.run_sync(starting_agent=last_agent,input="2+2")

print(res.final_output)