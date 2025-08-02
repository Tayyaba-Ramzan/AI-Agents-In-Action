from agents import function_tool

@function_tool
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