from agents import Runner,set_tracing_disabled,InputGuardrailTripwireTriggered,OutputGuardrailTripwireTriggered,SQLiteSession
from user_data_type.user_data import UserDataType
from my_agents.guardrial_agent import guardrial_agent
# from my_agents.math_agent import hotel_assistant
from my_agents.math_agent import assistant
import asyncio

set_tracing_disabled(True)

# session=SQLiteSession("user_3","conversation.db")

result=Runner.run_sync(assistant,"15-5")
print(result.final_output)

# async def main():
#     await session.clear_session()

# async def  main():
#     new_items = [
#     {"role": "user", "content": "Hello"},
#     {"role": "assistant", "content": "Hi there!"}
# ]
#     await session.add_items(new_items)

# asyncio.run(main())

# async def main():
#     user_data=await session.get_items()
#     for user in user_data:
#         print(f"{user['role']}: {user['content']}")

# asyncio.run(main())

# while True: 
#     prompt=input("Write Prompt Here:")

#     if prompt=="exit":
#         break

#     res=Runner.run_sync(starting_agent=assistant,input=prompt,session=session)
#     print(res.final_output)

# user1=UserDataType("Muhammmad Hassan",27,"Software Engineer")

# try:
#     res=Runner.run_sync(starting_agent=hotel_assistant,input="How many rooms availabe in Mehran Hotel?",context=user1)
#     # print(res.last_agent)
#     print(res.final_output)
# except InputGuardrailTripwireTriggered as e:
#     print(f"Trip Input Triggered------------> \n {e}")

# except OutputGuardrailTripwireTriggered as e:
#     print(f"Trip Output Triggered------------> \n {e}")