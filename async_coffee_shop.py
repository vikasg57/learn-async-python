import asyncio
import time


async def make_espresso():
    print("start preparing espresso")
    await asyncio.sleep(3)
    print(f"espresso done!")
    return "espresso"


async def make_latte():
    print("start preparing latte")
    await asyncio.sleep(5)
    print(f"latte done!")
    return "latte"


async def make_cappuccino():
    print("start preparing cappuccino")
    await asyncio.sleep(4)
    print(f"cappuccino done!")
    return "cappuccino"


async def coffee_shop():
    start_time = time.time()
    # Your code here - use asyncio.gather()
    await asyncio.gather(make_espresso(), make_latte(), make_cappuccino())
    total_time = time.time() - start_time
    print(f"All drinks prepared in {total_time:.1f} seconds")


# Run your coffee shop
asyncio.run(coffee_shop())


async def make_drinks(name, drink, duration):
    await asyncio.sleep(duration)
    print(f"start preparing {drink} for {name} waiting time {duration}")


async def coffee_shop_with_customers():
    customers = [
        ("Ram", "espresso", 3),
        ("Sham", "latte", 5),
        ("Teena", "cappuccino", 4),
        ("Meena", "cappuccino", 4),
    ]
    print("=== Coffee Shop Open ===\n")
    start_time = time.time()

    tasks = [make_drinks(customer, drink, duration) for customer, drink, duration in customers]
    results = await asyncio.gather(*tasks)

    total_time = time.time() - start_time
    print(f"\n=== All orders complete in {total_time:.1f} seconds ===")
    print("Orders served:", len(results))

# Run your coffee shop
asyncio.run(coffee_shop_with_customers())
