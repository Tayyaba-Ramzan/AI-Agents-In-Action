from agents import RunContextWrapper
from user_data_type.user_data import MyInputData

async def service(ctx:RunContextWrapper,input_data:MyInputData):
    return input_data.advice
    