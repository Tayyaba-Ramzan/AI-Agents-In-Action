from agents import Runner,set_tracing_disabled
from my_agents.math_agent import my_assistant

set_tracing_disabled(True)

res=Runner.run_sync(starting_agent=my_assistant,input="hello!")

print(res.last_agent)
print(res.final_output)