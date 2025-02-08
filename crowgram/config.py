from dotenv import load_dotenv
from os import getenv

load_dotenv()

# Required Variables
API_ID: int = int(os.getenv("API_ID", 7249983))

API_HASH: str = os.getenv("API_HASH", "be8ea36c220d5e879c91ad9731686642")

STRING_SESSION: str = os.getenv("STRING_SESSION", "BQBuoD8AuTI0qg2FHVUmNjJn_prTBuZPGkRs76iKazfwNytYFXeN4bZJ3N_NAh7eFnic_mRIuTP2mXyFlBFR0XxTIjaXiB26hRtg_qfZ-dWT2UslBACBpn7ifYB4YPnx7wVM7t05HSdp1S0F72PhIrA1UCwYroWkbMdn8Xa3IU1AbqEabViWxHJ09mwRYmiybRgwU-EQgLG-PgsIRK7iqHRrufOuGCgW_sxOWuuI8c6Z_qO3OntrzAtoFkPboIHRS6CLddEI0p6RqY7_zSJjBC5IyjmVS--9jKbhFpb6uVDXJ9a7eaxFLv7Rq9N9_wMNylqAgcTPUufybNWTOxl_ao_xaIDjwgAAAAFklkDwAA")

OWNER_ID: list[int] = [int(os.getenv("OWNER_ID", 7143123520))]

LOG_GROUP_ID: int = int(os.getenv("LOG_GROUP_ID", -4694535872))


# Optional Variables
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". ! /").split())


# Don't Change After This Line.
COMMAND_HANDLERS = []
for x in COMMAND_PREFIXES:
    COMMAND_HANDLERS.append(x)
COMMAND_HANDLERS.append('')
