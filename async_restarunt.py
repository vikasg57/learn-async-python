import asyncio
import random
import time


async def prepare_appetizer(order_id):
    """Prepare appetizer (1-2 seconds)"""
    # Your code here
    start_time = time.time()
    preparation_time = random.uniform(1, 2)
    print(f"Preparing appetizer for {order_id}...")
    await asyncio.sleep(preparation_time)
    final_time = time.time() - start_time
    print(f"Appetizer Ready for {order_id}in {final_time: .2f}")
    return final_time  # Return the time for tracking


async def prepare_main_course(order_id):
    """Prepare main course (3-5 seconds)"""
    # Your code here
    start_time = time.time()
    preparation_time = random.uniform(3, 5)
    print(f"Preparing main course for {order_id}...")
    await asyncio.sleep(preparation_time)
    final_time = time.time() - start_time
    print(f"Main Course Ready for {order_id}in {final_time: .2f}")
    return final_time  # Return the time for tracking


async def prepare_dessert(order_id):
    """Prepare dessert (1-3 seconds)"""
    start_time = time.time()
    preparation_time = random.uniform(1, 3)
    print(f"Preparing dessert for {order_id}...")
    await asyncio.sleep(preparation_time)
    final_time = time.time() - start_time
    print(f"Dessert Ready for {order_id} in {final_time: .2f}")
    return final_time  # Return the time for tracking


async def process_order(order_id, customer_name):
    """
    Process a complete order for a customer.
    All parts should be prepared simultaneously.
    """

    start_time = time.time()
    print(f"Starting order {order_id} for {customer_name}")

    # Using create_task for better control (as suggested in hints)
    appetizer_task = asyncio.create_task(prepare_appetizer(order_id))
    main_task = asyncio.create_task(prepare_main_course(order_id))
    dessert_task = asyncio.create_task(prepare_dessert(order_id))

    # Wait for all tasks to complete
    appetizer_time = await appetizer_task
    main_time = await main_task
    dessert_time = await dessert_task

    # Track individual times (as suggested in hints)
    final_time = time.time() - start_time
    print(f"🔔 Order {order_id} complete for {customer_name} in {final_time:.2f}")
    print(f"   Individual times - Appetizer: {appetizer_time:.2f}s, "
          f"Main: {main_time:.2f}s, Dessert: {dessert_time:.2f}s")
    return final_time


async def restaurant():
    orders = [
        (1, "Alice"),
        (2, "Bob"),
        (3, "Charlie"),
        (4, "Diana")
    ]

    # Create tasks for all orders (better control as per hints)
    order_tasks = []
    for order_id, customer_name in orders:
        task = asyncio.create_task(process_order(order_id, customer_name))
        order_tasks.append(task)

    order_times = await asyncio.gather(*order_tasks)

    # Summary statistics (tracking as suggested)
    print(f"\n=== Restaurant Summary ===")
    print(f"Total orders processed: {len(orders)}")
    print(f"Average order time: {sum(order_times)/len(order_times):.2f}s")
    print(f"Fastest order: {min(order_times):.2f}s")
    print(f"Slowest order: {max(order_times):.2f}s")


asyncio.run(restaurant())
