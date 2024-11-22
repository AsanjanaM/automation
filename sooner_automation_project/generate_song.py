import httpx
import json

async def generate_song():
    url = "https://api.sooner.com/song/generate"
    with open("session_cookies.json", "r") as file:
        cookies = json.load(file)

    headers = {"Authorization": "Bearer your_token", "Content-Type": "application/json"}
    data = {"song_title": "My New Song", "artist": "Myself", "genre": "Pop"}

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=data, cookies=cookies, headers=headers)
        if response.status_code == 200:
            song_uuid = response.json().get("uuid")
            return song_uuid
        else:
            print(f"Failed to generate song: {response.text}")
