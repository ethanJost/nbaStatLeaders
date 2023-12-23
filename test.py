import asyncio
from playwright.async_api import async_playwright, Playwright
import os

async def run(playwright: Playwright):
    chromium = playwright.chromium
    browser = await chromium.launch()
    page = await browser.new_page()
    await page.goto("https://www.basketball-reference.com/leagues/NBA_2024_advanced.html")
    # other actions...
    name_elements = await page.query_selector_all('td[data-stat="player"]')
    vorp_elements = await page.query_selector_all('td[data-stat="vorp"]')
    if len(name_elements) != len(vorp_elements):
        print("Mismatch in the number of player and VORP elements")
        return
    
    for name_element, vorp_element in zip(name_elements, vorp_elements):
        try:
            player_name = await name_element.text_content()
            player_vorp = await vorp_element.text_content()
            print(f"{player_name}: {player_vorp}")
        except Exception as e:
            print(f"Error processing element: {e}")
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())