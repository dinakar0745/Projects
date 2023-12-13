import asyncio
from truecallerpy import login

phone_number = "+1234567890"
response = asyncio.run(login(phone_number))
print(response)