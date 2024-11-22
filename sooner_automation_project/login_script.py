import asyncio
import httpx
import json
from playwright.sync_api import sync_playwright

# 1. Automate Login with Playwright
def login_with_google():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.sooner.com/login")
        page.click('text="Login with Google"')
        page.wait_for_url("https://accounts.google.com/")
        page.fill('input[type="email"]', "your_email@gmail.com")
        page.click('button[jsname="LgbsSe"]')
        page.fill('input[type="password"]', "your_password")
        page.click('button[jsname="LgbsSe"]')
        page.wait_for_url("https://www.sooner.com/dashboard")
        cookies = page.context.cookies()
        with open("session_cookies.json", "w") as file:
            json.dump(cookies, file)
        browser.close()
