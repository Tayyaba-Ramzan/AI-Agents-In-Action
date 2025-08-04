from agents import function_tool,RunContextWrapper
from user_data_type.user_data import UserDataType

@function_tool
def get_age(ctx:RunContextWrapper[UserDataType]):
    """Age funciton"""
    print("Age tool fire-------------->")
    return f"your age is {ctx.context.age}"