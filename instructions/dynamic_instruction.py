from agents import RunContextWrapper,Agent
from  user_data_type.user_data import UserDataType

def dynamic_instruction(ctx:RunContextWrapper[UserDataType],agent:Agent[UserDataType]):
    return f"user name is {ctx.context.name,} you are a helpfull assistant"