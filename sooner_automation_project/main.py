import asyncio
import json
from login_script import login_with_google
from generate_song import generate_song
from check_song_status import check_song_status

# Main Execution
async def main():
    login_with_google()  # Automate the login process
    song_uuid = await generate_song()  # Send song generation request
    await check_song_status(song_uuid)  # Continuously check song status

asyncio.run(main())
