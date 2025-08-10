from agents import RunContextWrapper,GuardrailFunctionOutput,output_guardrail,Runner,Agent,TResponseInputItem
from my_agents.guardrial_agent import guardrial_agent

@output_guardrail
async def guardrial_output_function(ctx:RunContextWrapper[None],agent:Agent,input:str|list[TResponseInputItem])->GuardrailFunctionOutput:
    response=await Runner.run(guardrial_agent,input,context=ctx.context)
    print(agent.name)
    return GuardrailFunctionOutput(
        output_info=response.final_output,
        tripwire_triggered=response.final_output.is_hotel_mehran_account_or_tax_query
    )