import asyncio
import random
import time
from typing import List, Tuple


async def process_task(task_id: str, duration: float, priority: str):
    """
    Process a single task
    """
    start_time = time.time()
    print(f"Starting {task_id}")
    await asyncio.sleep(duration)
    elapsed = time.time() - start_time
    print(f"✓ {task_id} completed {elapsed: .2f}")
    return elapsed


async def process_priority_batch(tasks: List[Tuple[str, float, str]], priority: str):
    """
    Process all tasks of a given priority simultaneously
    """
    print(f"\n[{priority.upper()} PRIORITY BATCH]")
    start_time = time.time()

    batch = []
    for task_id, duration, priority in tasks:
        batch.append(asyncio.create_task(process_task(task_id, duration, priority)))

    # Wait for all tasks in this batch to complete
    results = await asyncio.gather(*batch)

    batch_time = time.time() - start_time
    print(f"{priority.capitalize()} priority batch completed in {batch_time:.1f}s")

    return results


async def task_scheduler():
    # Create tasks with (id, duration, priority)
    high_priority_tasks = [
        (f"HIGH-{i}", random.uniform(1, 2), "high")
        for i in range(1, 4)
    ]

    low_priority_tasks = [
        (f"LOW-{i}", random.uniform(2, 4), "low")
        for i in range(1, 6)
    ]

    print("=== Task Scheduler Started ===\n")

    overall_start = time.time()

    # Process HIGH priority first, THEN LOW priority (sequential batches)
    high_results = await process_priority_batch(high_priority_tasks, "high")
    low_results = await process_priority_batch(low_priority_tasks, "low")

    total_time = time.time() - overall_start

    # Calculate statistics
    all_times = high_results + low_results
    high_avg = sum(high_results) / len(high_results)
    low_avg = sum(low_results) / len(low_results)

    print(f"\n=== Scheduler Summary ===")
    print(f"Total tasks: {len(all_times)}")
    print(f"Total time: {total_time:.1f} seconds")
    print(f"High priority avg: {high_avg:.1f}s")
    print(f"Low priority avg: {low_avg:.1f}s")


asyncio.run(task_scheduler())
