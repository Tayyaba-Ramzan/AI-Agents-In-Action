from agents import Agent
from my_config.gemini_config import model
from user_data_type.user_data import HotelDataType

guardrial_agent=Agent(
    name="guardrial_agent",
    instructions="Check Hotel Mehran queries and account or tax query.",
    model=model,
    output_type=HotelDataType
)