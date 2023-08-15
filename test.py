from bot import MidlandBot
from selenium.webdriver.common.by import By
import time


test_bot = MidlandBot()

test_bot.get_results_for_city()

print("Waiting for page to load...")
time.sleep(10)

results = test_bot.get_listings_for_today()

print(results)
# for item in results:
#     print(item)
#     print(item)

listing_available = False

while not listing_available:

    # get listings for today
    test_bot.driver.refresh()

    valid_results = test_bot.get_listings_for_today()
    is_listing_available = test_bot.keep_checking_for_listing(valid_results)

    if len(valid_results) == 0:
        print("No Valid Listing for today...")
        break

    for listing in valid_results:

        # check if the listing has become available
        listing_description_2 = listing['sel_object'].find_element(By.CLASS_NAME, "text-neutral-6")
        if listing['available']:
            print("Listing has become available... Preparing to place order")
            listing_available = True

            test_bot.login_to_website()
            print(listing['name'])

            test_bot.open_listing(name=listing['name'])
            time.sleep(3)

            if test_bot.listing_page_loaded():
                break
            else:
                success = test_bot.listing_page_loaded()
                if success:
                    break
                else:

                    # Try Again
                    test_bot.driver.close()
                    test_bot.driver.switch_to.window(test_bot.driver.window_handles[0])
                    time.sleep(30)
                    print("Trying to open listing again...")
                    test_bot.open_listing(listing['name'])
                    success = test_bot.listing_page_loaded()
                    if success:
                        break
                    else:
                        print("Failed to locate header in listing homepage...")
                    break
        else:
            print("Listing still not available...")



time.sleep(1000)
