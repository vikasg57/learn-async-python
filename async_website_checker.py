import asyncio
import random
import time


async def check_website_with_retry(url, max_retries = 2):
    """Check website with retry on failure"""
    for attempt in range(max_retries + 1):
        print(f"Checking {url}... (attempt {attempt + 1})")

        delay = random.uniform(1, 3)
        await asyncio.sleep(delay)

        is_online = random.random() < 0.8

        if is_online:
            print(f"✅ {url} is online")
            return True
        elif attempt < max_retries:
            print(f"⚠️ {url} is offline, retrying...")
        else:
            print(f"❌ {url} is offline after {max_retries + 1} attempts")
            return False


async def monitor_websites():
    websites = [
        "google.com",
        "github.com",
        "stackoverflow.com",
        "python.org",
        "asyncio-docs.com"
    ]
    start_time = time.time()

    # Your code here:
    # 1. Check all websites simultaneously
    tasks = [check_website_with_retry(url) for url in websites]
    results = await asyncio.gather(*tasks)
    total_time = time.time() - start_time
    print(f"\n=== All website checking complete in {total_time:.1f} seconds ===")
    [print("website checked:", result) for result in results]


asyncio.run(monitor_websites())
