import httpx
import asyncio

async def check_song_status(song_uuid):
    url = f"https://api.sooner.com/song/status/{song_uuid}"

    async with httpx.AsyncClient() as client:
        while True:
            response = await client.get(url)
            if response.status_code == 200:
                status = response.json().get("status")
                print(f"Song status: {status}")
                if status == "Completed":
                    print("Song generation completed!")
                    break
            else:
                print(f"Failed to check status: {response.text}")
            await asyncio.sleep(10)
