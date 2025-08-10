from agents import RunContextWrapper,GuardrailFunctionOutput,Runner,input_guardrail,Agent,TResponseInputItem
from my_agents.guardrial_agent import guardrial_agent

@input_guardrail
async def guardrial_input_function(ctx:RunContextWrapper[None],agent:Agent,input:str|list[TResponseInputItem])->GuardrailFunctionOutput:
    response=await Runner.run(guardrial_agent,input,context=ctx.context)
    print(agent.name)
    return GuardrailFunctionOutput(
        output_info=response.final_output,
        tripwire_triggered=not response.final_output.is_query_about_mehran_hotel
    )