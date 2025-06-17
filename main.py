from webscraper import WebScraperAgent
import asyncio

async def webscraper(target_url, base_url):
    result = None
    try:
        print('Extracting HTML Content...')
        html_content = await scraper.scrape_content(target_url)

        print('Taking Screenshot...')
        screenshot = await scraper.screenshot_buffer()

        print(html_content[:1000])  # Print first 1000 characters of HTML content
        print('Screenshot taken successfully.')
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        await scraper.close()
        print('Browser closed.')
    return result

if __name__ == "__main__":
    scraper = WebScraperAgent()
    target_url = "https://www.deeplearning.ai/courses"
    base_url = "https://www.deeplearning.ai"

    result = asyncio.run(webscraper(target_url, base_url))