from dotenv import load_dotenv
from os import getenv
import os

load_dotenv()

# Required Variables
API_ID: int = int(os.getenv("API_ID", 7249983))

API_HASH: str = os.getenv("API_HASH", "be8ea36c220d5e879c91ad9731686642")

STRING_SESSION: str = os.getenv("STRING_SESSION", "BQBuoD8AQGKekLrK5vtrXbD14jAWzXEoiFDruzTpQWeWtbQidX6_Ald4YeAQGgN5VCVdqwrj8LE46F9ilDUmNZ3vYvVYrTe9hmY5BFPvXN2Lz8MtYPJgAouumlFaJ9V7YQ7BX5puBq9DHZ3TjtyR5AQ0MuNzQD3bHtYGQXOtUB0NezdjzbNxca-W2Zs2JTHOlvOKjFA_FXtta3OfG0XQjN5iBQNOHau7vGCmLAfsabg1s5RYvqop1k-kbgjuLDgT2Ypw3cT1vu5rVFRG1zNczKTQ1-33YrYC_ItnBGVE9LwYJoyO0zRAxDwmU3TjjgZqt8EJn5R6MYSXoXhpKhcA_aNWJK7zigAAAAFklkDwAA")

OWNER_ID: list[int] = [int(os.getenv("OWNER_ID", 7143123520))]

LOG_GROUP_ID: int = int(os.getenv("LOG_GROUP_ID", -4694535872))

BOT_TOKEN = getenv("BOT_TOKEN", None)

# Optional Variables
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". ! /").split())


# Don't Change After This Line.
COMMAND_HANDLERS = []
for x in COMMAND_PREFIXES:
    COMMAND_HANDLERS.append(x)
COMMAND_HANDLERS.append('')
