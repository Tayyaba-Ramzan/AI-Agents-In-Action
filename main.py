from agents import Runner,set_tracing_disabled
from my_agents.math_agent import first_agent

set_tracing_disabled(True)

res=Runner.run_sync(starting_agent=first_agent,input="2*5=?",max_turns=4)

print(res.final_output)