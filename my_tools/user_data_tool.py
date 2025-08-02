import requests
from agents import function_tool

@function_tool
def fetch_user_data()->list:
    """
    fetch function for user data and return list
    """
    url="https://jsonplaceholder.typicode.com/users"
    res=requests.get(url)
    return res.json()

@function_tool
def fetch_user_dat_by_id(id:int)->list:
    """
    fetch function for user data and return list
    """
    url=f"https://jsonplaceholder.typicode.com/users{id}"
    res=requests.get(url)
    return res.json()

