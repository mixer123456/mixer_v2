import os
from typing import Final

from dotenv import load_dotenv

load_dotenv()

TOKEN_UKR_NET: Final = os.getenv('TOKEN_UKR_NET')
USERS_EMAIL: Final = os.getenv('USERS_EMAIL')
USERNAME: Final = os.getenv('USERNAME')
STMP_SERVER: Final = os.getenv('STMP_SERVER')
