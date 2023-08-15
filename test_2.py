from bot import MidlandBot
from selenium.webdriver.common.by import By

import time

monitored_listings = []
monitoring_id = 3340

# Create the bot class
test_bot = MidlandBot()

# Login to the Midland bot website
test_bot.login_to_website()

# open the page for all listings in birmingham within a 20 mile radius
test_bot.get_results_for_city()

# Monitor the listing with the given id and click on the button when the listing becomes available.
test_bot.send_message_to_telegram(f'"Currently Monitoring Listing https://homes.midlandheart.org.uk/Search.PropertyDetails.aspx?PropertyId={monitoring_id}')
test_bot.monitor_listing(monitoring_id, 3)
time.sleep(3)

test_bot.pass_eligibility_stage()
time.sleep(5)
print(test_bot.driver.title)

test_bot.pass_preference_group()
time.sleep(5)
print(test_bot.driver.title)

test_bot.pass_evidence_stage()
time.sleep(5)
print(test_bot.driver.title)

test_bot.pass_contact_details()
time.sleep(5)
print(test_bot.driver.title)

test_bot.pass_extra_stage("JB321623C")
time.sleep(5)
print(test_bot.driver.title)

test_bot.pass_savings_income_stage()
time.sleep(5)
print(test_bot.driver.title)

test_bot.pass_equality_stage()
time.sleep(5)
print(test_bot.driver.title)

test_bot.pass_confirm_details_stage()
time.sleep(5)
print(test_bot.driver.title)
