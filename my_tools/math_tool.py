from agents import function_tool,FunctionTool,RunContextWrapper
from user_data_type.user_data import SubDataType

async def subtract_function(ctx:RunContextWrapper,args):
    obj=SubDataType.model_validate_json(args)
    return f"your sub result is {obj.n1-obj.n2}"

subtract=FunctionTool(
    name="subtract_tool",
    description="This is a subtract_tool",
    params_json_schema=SubDataType.model_json_schema(),
    on_invoke_tool=subtract_function,
    is_enabled=True
)

@function_tool
def weather_function(city:str):
    """This is a weather funciton"""
    return f"{city}: cloudly"

@function_tool(name_override="sum",description_override="This is a sum tool",is_enabled=True)
def add(n1:int,n2:int):
    """This is add funciton
    args:
        n1:int
        n2:int
    return:str

    """
    print("add tool fire---------------->")
    return f"your answer is {n1+n2}"

@function_tool
def sub(n1:int,n2:int):
    """This is sub funciton
    args:
        n1:int
        n2:int
    return:str

    """
    print("sub tool fire---------------->")
    return f"your answer is {n1-n2}"

@function_tool
def mul(n1:int,n2:int):
    """This is mul funciton
    args:
        n1:int
        n2:int
    return:str
    """
    print("mul tool fire---------------->")
    return f"your answer is {n1*n2}"

@function_tool
def div(n1:int,n2:int):
    """This is div funciton
    args:
        n1:int
        n2:int
    return:str

    """
    print("div tool fire---------------->")
    return f"your answer is {n1-n2}"