import asyncio
from playwright.async_api import async_playwright, Playwright
from Player import Player

async def run(playwright):

    chromium = playwright.chromium
    browser = await chromium.launch(headless=False)
    page = await browser.new_page()
    await page.goto('https://www.basketball-reference.com/leagues/NBA_2024_advanced.html', timeout=60000)
    num_players = await page.eval_on_selector_all('td[data-stat="player"]', "elements => elements.length")
    players = []
    for i in range(num_players):
        name_element = f"document.querySelectorAll('td[data-stat=\"player\"]')[{i}].textContent"
        pos_element = f"document.querySelectorAll('td[data-stat=\"pos\"]')[{i}].textContent"
        age_element = f"document.querySelectorAll('td[data-stat=\"age\"]')[{i}].textContent"
        team_element = f"document.querySelectorAll('td[data-stat=\"team_id\"]')[{i}].textContent"
        games_element = f"document.querySelectorAll('td[data-stat=\"g\"]')[{i}].textContent"
        mp_element = f"document.querySelectorAll('td[data-stat=\"mp\"]')[{i}].textContent"
        per_element = f"document.querySelectorAll('td[data-stat=\"per\"]')[{i}].textContent"
        ts_element = f"document.querySelectorAll('td[data-stat=\"ts_pct\"]')[{i}].textContent"
        usg_element = f"document.querySelectorAll('td[data-stat=\"usg_pct\"]')[{i}].textContent"
        ws_element = f"document.querySelectorAll('td[data-stat=\"ws\"]')[{i}].textContent"
        vorp_element = f"document.querySelectorAll('td[data-stat=\"vorp\"]')[{i}].textContent"
        try:
            name = await page.evaluate(name_element)
            vorp_text = await page.evaluate(vorp_element)
            pos_text = await page.evaluate(pos_element)
            age_text = await page.evaluate(age_element)
            team_text = await page.evaluate(team_element)
            games_text = await page.evaluate(games_element)
            mp_text = await page.evaluate(mp_element)
            per_text = await page.evaluate(per_element)
            ts_text = await page.evaluate(ts_element)
            usg_text = await page.evaluate(usg_element)
            ws_text = await page.evaluate(ws_element)
            try:
                vorp = float(vorp_text)
            except ValueError:
                vorp = None
            try:
                age = int(age_text)
            except ValueError:
                age = None
            try:
                games = int(games_text)
            except ValueError:
                games = None
            try:
                mp = int(mp_text)
            except ValueError:
                mp = None
            try:
                per = float(per_text)
            except ValueError:
                per = None
            try:
                ts = float(ts_text)
            except ValueError:
                ts = None
            try:
                usg = float(usg_text)
            except ValueError:
                usg = None
            try:
                ws = float(ws_text)
            except ValueError:
                ws = None
            
            

            player = Player(name, pos_text, age, team_text, games, mp, per, ts, usg, ws, vorp)
            players.append(player)
        except Exception as e:
            print(f"Error processing player at index {i}: {e}")
    with open('p_storage.txt', 'w') as f:
        for player in players:
            f.write(str(player))
            f.write("\n")
    
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())