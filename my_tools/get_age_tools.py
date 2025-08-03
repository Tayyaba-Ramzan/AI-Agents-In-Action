from agents import function_tool,RunContextWrapper

@function_tool
def get_age(ctx:RunContextWrapper):
    """Age funciton"""
    print("Age tool fire-------------->")
    return f"your age is {ctx.context["age"]}"