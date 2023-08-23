from bot import MidlandBot
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time

load_dotenv()

monitored_listings = []
monitoring_id = 3355

# Create the bot class
test_bot = MidlandBot(user_name=os.getenv('MH_USERNAME'),
                      password=os.getenv('MH_PASSWORD'),
                      monitoring_id=monitoring_id,
                      ni_number="JB321623C"
                      )
test_bot.start_bot()
