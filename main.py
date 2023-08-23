import argparse
from bot import MidlandBot
from dotenv import load_dotenv
import os


def run_bot():
    load_dotenv()

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Run the Midland Bot")
    parser.add_argument("username", type=str, help="Your username")
    parser.add_argument("password", type=str, help="Your password")
    parser.add_argument("monitoring_id", type=int, help="Monitoring ID")
    parser.add_argument("ni_number", type=str, help="NI number")
    args = parser.parse_args()

    # Create the bot class
    start_bot = MidlandBot(user_name=args.username,
                           password=args.password,
                           monitoring_id=args.monitoring_id,
                           ni_number=args.ni_number
                           )
    start_bot.start_bot()


if __name__ == "__main__":
    run_bot()
