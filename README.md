# Async Python Learning Exercises 🚀

A collection of hands-on exercises to master asynchronous programming in Python.

---

## 📚 Table of Contents
- [Exercise 1: Coffee Shop Simulator](#exercise-1-coffee-shop-simulator-)
- [Exercise 2: Website Status Checker](#exercise-2-website-status-checker-)
- [Exercise 3: Download Manager](#exercise-3-download-manager-)
- [Exercise 4: Restaurant Order System](#exercise-4-restaurant-order-system-)
- [Exercise 5: Task Scheduler with Priorities](#exercise-5-task-scheduler-with-priorities-)
- [Async Python Cheatsheet](#async-python-cheatsheet-)

---

## Exercise 1: Coffee Shop Simulator ☕

### Difficulty: Beginner

### Learning Objectives
- Practice basic `async`/`await` syntax
- Use `asyncio.gather()` for concurrent execution
- Understand time measurement in async programs

### Problem Statement
You are building a coffee shop simulation where multiple baristas can prepare different drinks simultaneously. Each drink takes a different amount of time to prepare.

### Requirements

#### Functional Requirements
1. Create three async functions:
   - `make_espresso()`: Takes 3 seconds to prepare
   - `make_latte()`: Takes 5 seconds to prepare
   - `make_cappuccino()`: Takes 4 seconds to prepare

2. Each function should:
   - Print when it starts making the drink
   - Simulate preparation time using `asyncio.sleep()`
   - Print when the drink is ready
   - Return the drink name

3. Create a main function `coffee_shop()` that:
   - Starts all three drink preparations simultaneously
   - Waits for all drinks to be ready
   - Prints the total time taken

#### Expected Output
```
Starting to make Espresso...
Starting to make Latte...
Starting to make Cappuccino...
Espresso is ready!
Cappuccino is ready!
Latte is ready!
All drinks prepared in 5.0 seconds
```

### Starter Code
```python
import asyncio
import time

async def make_espresso():
    # Your code here
    pass

async def make_latte():
    # Your code here
    pass

async def make_cappuccino():
    # Your code here
    pass

async def coffee_shop():
    start_time = time.time()
    
    # Your code here - use asyncio.gather()
    
    total_time = time.time() - start_time
    print(f"All drinks prepared in {total_time:.1f} seconds")

# Run your coffee shop
asyncio.run(coffee_shop())
```

### Hints
- Use `time.time()` to measure total execution time
- Remember to `await` async functions
- `asyncio.gather()` can run multiple coroutines concurrently

### Bonus Challenges
1. Add random preparation times (2-6 seconds per drink)
2. Add a customer name parameter to each drink
3. Implement a queue system for multiple orders

---

## Exercise 2: Website Status Checker 🌐

### Difficulty: Beginner-Intermediate

### Learning Objectives
- Practice async loops
- Implement error handling
- Work with random delays and results
- Process multiple async operations

### Problem Statement
Create a website monitoring system that checks multiple websites' status simultaneously. The checker should simulate network delays and random failures.

### Requirements

#### Functional Requirements
1. Create an async function `check_website(url)`:
   - Print "Checking {url}..."
   - Simulate network delay (random 1-3 seconds)
   - Return True (80% probability) or False (20% probability)
   - Print "✅ {url} is online" or "❌ {url} is offline"

2. Create main function `monitor_websites()`:
   - Check 5 websites simultaneously
   - Count online vs offline sites
   - Print summary statistics

#### Expected Output
```
Checking google.com...
Checking github.com...
Checking stackoverflow.com...
Checking python.org...
Checking asyncio-docs.com...
✅ github.com is online
✅ google.com is online
❌ stackoverflow.com is offline
✅ python.org is online
✅ asyncio-docs.com is online

=== Website Status Report ===
Online: 4/5
Offline: 1/5
Response time: 2.3 seconds
```

### Starter Code
```python
import asyncio
import random

async def check_website(url):
    """
    Simulate checking a website.
    Returns True if online, False if offline
    """
    # Your code here:
    # 1. Print "Checking {url}..."
    # 2. Wait random time between 1-3 seconds
    # 3. Randomly return True (80% chance) or False (20% chance)
    pass

async def monitor_websites():
    websites = [
        "google.com",
        "github.com",
        "stackoverflow.com",
        "python.org",
        "asyncio-docs.com"
    ]
    
    # Your code here:
    # 1. Check all websites simultaneously
    # 2. Print results
    pass

asyncio.run(monitor_websites())
```

### Hints
- Use `random.uniform(1, 3)` for delays
- Use `random.random() < 0.8` for 80% probability
- Store results as tuples: (url, status)
- Use `asyncio.gather()` with return values

### Bonus Challenges
1. Add retry logic for failed checks
2. Implement timeout handling
3. Add response time per website
4. Create a continuous monitoring loop

---

## Exercise 3: Download Manager 📥

### Difficulty: Intermediate

### Learning Objectives
- Compare sequential vs parallel execution
- Show progress for async operations
- Calculate performance improvements
- Work with different file sizes

### Problem Statement
Build a download manager that can download files either sequentially (one after another) or in parallel (all at once). Compare the performance difference.

### Requirements

#### Functional Requirements
1. Create `download_file(filename, size_mb)`:
   - Calculate download time: 100MB = 1 second
   - Show progress: "Downloading {filename} ({size_mb}MB)..."
   - Print completion: "✓ {filename} downloaded in {time}s"
   - Return tuple: (filename, size_mb, time_taken)

2. Implement `sequential_download(files)`:
   - Download files one by one
   - Show total progress
   - Return total time

3. Implement `parallel_download(files)`:
   - Download all files simultaneously
   - Show individual progress
   - Return total time

#### Expected Output
```
=== Sequential Download ===
Downloading movie.mp4 (500MB)...
✓ movie.mp4 downloaded in 5.0s
Downloading music.mp3 (50MB)...
✓ music.mp3 downloaded in 0.5s
[... more files ...]
Sequential total: 8.65 seconds

=== Parallel Download ===
Downloading movie.mp4 (500MB)...
Downloading music.mp3 (50MB)...
Downloading document.pdf (10MB)...
Downloading image.jpg (5MB)...
Downloading archive.zip (300MB)...
✓ image.jpg downloaded in 0.05s
✓ document.pdf downloaded in 0.1s
✓ music.mp3 downloaded in 0.5s
✓ archive.zip downloaded in 3.0s
✓ movie.mp4 downloaded in 5.0s
Parallel total: 5.0 seconds

=== Performance Summary ===
Sequential: 8.65 seconds
Parallel: 5.00 seconds
Speed improvement: 1.73x faster
```

### Starter Code
```python
import asyncio
import time

async def download_file(filename, size_mb):
    """
    Simulate downloading a file.
    size_mb: size in megabytes
    Returns: (filename, size_mb, time_taken)
    """
    # Your code here
    pass

async def sequential_download(files):
    """Download files one by one"""
    print("\n=== Sequential Download ===")
    start = time.time()
    
    # Your code here
    
    return time.time() - start

async def parallel_download(files):
    """Download files simultaneously"""
    print("\n=== Parallel Download ===")
    start = time.time()
    
    # Your code here
    
    return time.time() - start

async def main():
    files = [
        ("movie.mp4", 500),
        ("music.mp3", 50),
        ("document.pdf", 10),
        ("image.jpg", 5),
        ("archive.zip", 300)
    ]
    
    # Run both methods and compare times
    seq_time = await sequential_download(files)
    par_time = await parallel_download(files)
    
    print(f"\n=== Performance Summary ===")
    print(f"Sequential: {seq_time:.2f} seconds")
    print(f"Parallel: {par_time:.2f} seconds")
    print(f"Speed improvement: {seq_time/par_time:.2f}x faster")

asyncio.run(main())
```

### Hints
- Download time = size_mb / 100
- Use `asyncio.gather()` for parallel downloads
- Track start time with `time.time()`

### Bonus Challenges
1. Add bandwidth limiting
2. Implement pause/resume functionality
3. Add progress bars with percentages
4. Simulate download failures and retries

---

## Exercise 4: Restaurant Order System 🍽️

### Difficulty: Intermediate

### Learning Objectives
- Coordinate multiple async operations
- Handle complex workflows
- Process multiple orders simultaneously
- Work with different timing requirements

### Problem Statement
Create a restaurant order processing system where different kitchen stations prepare parts of an order concurrently. Multiple customer orders should be processed simultaneously.

### Requirements

#### Functional Requirements
1. Kitchen Stations (async functions):
   - `prepare_appetizer(order_id)`: 1-2 seconds
   - `prepare_main_course(order_id)`: 3-5 seconds  
   - `prepare_dessert(order_id)`: 1-3 seconds

2. Order Processing:
   - `process_order(order_id, customer_name)`:
     - Start all three preparations simultaneously
     - Wait for all items to complete
     - Print order ready notification

3. Restaurant System:
   - Process multiple customer orders concurrently
   - Track total service time
   - Show when each order completes

#### Expected Output
```
=== Restaurant Opening ===
Starting order 1 for Alice
Starting order 2 for Bob
Starting order 3 for Charlie
Starting order 4 for Diana

Preparing appetizer for order 1...
Preparing main course for order 1...
Preparing dessert for order 1...
[... similar for other orders ...]

✓ Appetizer ready for order 2 (1.3s)
✓ Dessert ready for order 1 (1.5s)
✓ Appetizer ready for order 3 (1.7s)
[... more completions ...]

🔔 Order 1 complete for Alice! (4.5s)
🔔 Order 3 complete for Charlie! (4.8s)
🔔 Order 2 complete for Bob! (5.1s)
🔔 Order 4 complete for Diana! (5.3s)

=== Service Complete ===
All orders served in 5.3 seconds
Average order time: 4.9 seconds
```

### Starter Code
```python
import asyncio
import random

async def prepare_appetizer(order_id):
    """Prepare appetizer (1-2 seconds)"""
    # Your code here
    pass

async def prepare_main_course(order_id):
    """Prepare main course (3-5 seconds)"""
    # Your code here
    pass

async def prepare_dessert(order_id):
    """Prepare dessert (1-3 seconds)"""
    # Your code here
    pass

async def process_order(order_id, customer_name):
    """
    Process a complete order for a customer.
    All parts should be prepared simultaneously.
    """
    print(f"Starting order {order_id} for {customer_name}")
    
    # Your code here:
    # 1. Prepare all three items simultaneously
    # 2. Wait for all to complete
    # 3. Print when order is ready
    
    pass

async def restaurant():
    orders = [
        (1, "Alice"),
        (2, "Bob"),
        (3, "Charlie"),
        (4, "Diana")
    ]
    
    # Process all orders simultaneously
    # Your code here
    pass

asyncio.run(restaurant())
```

### Hints
- Use `random.uniform()` for cooking times
- Use nested `asyncio.gather()` calls
- Track individual order times
- Consider using `asyncio.create_task()` for better control

### Bonus Challenges
1. Add kitchen capacity limits (max 2 main courses at once)
2. Implement order priorities (VIP customers)
3. Add order modifications mid-preparation
4. Create a kitchen load balancer

---

## Exercise 5: Task Scheduler with Priorities ⚡

### Difficulty: Advanced

### Learning Objectives
- Implement priority-based execution
- Use `asyncio.create_task()`
- Manage task batches
- Track detailed execution metrics

### Problem Statement
Build a task scheduler that processes tasks based on priority levels. High-priority tasks should complete before low-priority tasks begin.

### Requirements

#### Functional Requirements
1. Task Structure:
   - Task ID (e.g., "HIGH-1", "LOW-1")
   - Duration (seconds)
   - Priority ("high" or "low")

2. Processing Rules:
   - All high-priority tasks run simultaneously
   - Low-priority tasks start only after high-priority complete
   - Track individual task times
   - Show real-time progress

3. Metrics:
   - Total execution time
   - Average time per priority level
   - Task completion order

#### Expected Output
```
=== Task Scheduler Started ===

[HIGH PRIORITY BATCH]
Starting HIGH-1 (1.5s)
Starting HIGH-2 (1.8s)
Starting HIGH-3 (1.2s)
✓ HIGH-3 completed (1.2s)
✓ HIGH-1 completed (1.5s)
✓ HIGH-2 completed (1.8s)
High priority batch completed in 1.8s

[LOW PRIORITY BATCH]
Starting LOW-1 (2.5s)
Starting LOW-2 (3.0s)
Starting LOW-3 (2.2s)
Starting LOW-4 (3.5s)
Starting LOW-5 (2.8s)
✓ LOW-3 completed (2.2s)
✓ LOW-1 completed (2.5s)
✓ LOW-5 completed (2.8s)
✓ LOW-2 completed (3.0s)
✓ LOW-4 completed (3.5s)
Low priority batch completed in 3.5s

=== Scheduler Summary ===
Total tasks: 8
Total time: 5.3 seconds
High priority avg: 1.5s
Low priority avg: 2.8s
```

### Starter Code
```python
import asyncio
import random
from typing import List, Tuple

async def process_task(task_id: str, duration: float, priority: str):
    """
    Process a single task
    """
    # Your code here
    pass

async def process_priority_batch(tasks: List[Tuple[str, float, str]], priority: str):
    """
    Process all tasks of a given priority simultaneously
    """
    # Your code here
    pass

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
    
    # Your code here:
    # 1. Process all high priority tasks first (simultaneously)
    # 2. Then process all low priority tasks (simultaneously)
    # 3. Measure and print total time
    
    pass

asyncio.run(task_scheduler())
```

### Hints
- Use separate functions for each priority batch
- Consider using `asyncio.as_completed()` for progress
- Track timing at multiple levels
- Use colored output for better visualization (optional)

### Bonus Challenges
1. Add medium priority level
2. Implement task dependencies
3. Add task cancellation capability
4. Create dynamic priority adjustment
5. Implement task retry on failure

---

## Async Python Cheatsheet 📋

### Basic Syntax

#### Creating Async Functions
```python
# Define async function
async def my_function():
    await asyncio.sleep(1)
    return "Done"

# Call async function
result = await my_function()  # Inside async function
result = asyncio.run(my_function())  # From sync code
```

#### Essential Imports
```python
import asyncio
import time
from typing import List, Tuple, Optional
```

### Core Patterns

#### 1. Run Multiple Tasks Concurrently
```python
# Using gather
results = await asyncio.gather(
    task1(),
    task2(),
    task3()
)

# Using create_task
task1 = asyncio.create_task(coroutine1())
task2 = asyncio.create_task(coroutine2())
result1 = await task1
result2 = await task2
```

#### 2. Sequential vs Concurrent
```python
# Sequential (slow)
async def sequential():
    result1 = await task1()  # Wait
    result2 = await task2()  # Then wait
    return result1, result2

# Concurrent (fast)
async def concurrent():
    results = await asyncio.gather(
        task1(),
        task2()
    )
    return results
```

#### 3. Timeout Handling
```python
try:
    result = await asyncio.wait_for(
        long_running_task(),
        timeout=5.0
    )
except asyncio.TimeoutError:
    print("Task timed out!")
```

#### 4. Error Handling
```python
# In gather
results = await asyncio.gather(
    task1(),
    task2(),
    return_exceptions=True  # Don't fail on exception
)

# Individual try-except
async def safe_task():
    try:
        return await risky_operation()
    except Exception as e:
        print(f"Error: {e}")
        return None
```

#### 5. Running in Batches
```python
async def process_batch(items, batch_size=5):
    for i in range(0, len(items), batch_size):
        batch = items[i:i + batch_size]
        results = await asyncio.gather(
            *[process_item(item) for item in batch]
        )
        yield results
```

#### 6. Progress Tracking
```python
async def with_progress(tasks):
    for coro in asyncio.as_completed(tasks):
        result = await coro
        print(f"Completed: {result}")
```

### Common Functions

| Function | Purpose | Example |
|----------|---------|---------|
| `asyncio.run()` | Run async function from sync code | `asyncio.run(main())` |
| `asyncio.sleep()` | Async delay | `await asyncio.sleep(1)` |
| `asyncio.gather()` | Run multiple coroutines | `await asyncio.gather(task1(), task2())` |
| `asyncio.create_task()` | Schedule coroutine | `task = asyncio.create_task(coro())` |
| `asyncio.wait_for()` | Set timeout | `await asyncio.wait_for(coro(), timeout=5)` |
| `asyncio.as_completed()` | Process as tasks complete | `for coro in asyncio.as_completed(tasks):` |

### Do's and Don'ts

#### ✅ DO:
- Use `asyncio.sleep()` for delays in async functions
- Use `await` when calling async functions
- Use `asyncio.gather()` for concurrent execution
- Handle exceptions properly
- Use type hints for clarity

#### ❌ DON'T:
- Use `time.sleep()` in async functions (blocks everything)
- Forget `await` keyword (creates coroutine object)
- Mix sync and async carelessly
- Create event loops manually (use `asyncio.run()`)
- Ignore exceptions in concurrent tasks

### Common Errors and Solutions

#### Error: "coroutine was never awaited"
```python
# Wrong
async def main():
    my_async_function()  # Missing await!

# Correct
async def main():
    await my_async_function()
```

#### Error: "asyncio.run() cannot be called from a running event loop"
```python
# Wrong - nested asyncio.run()
async def outer():
    asyncio.run(inner())  # Can't nest!

# Correct
async def outer():
    await inner()  # Use await instead
```

#### Error: "This event loop is already running"
```python
# This happens in Jupyter notebooks
# Solution: Use await directly or nest_asyncio
import nest_asyncio
nest_asyncio.apply()
```

### Performance Tips

1. **Use gather for known tasks**
   ```python
   # Good for fixed number of tasks
   results = await asyncio.gather(*tasks)
   ```

2. **Use create_task for dynamic tasks**
   ```python
   # Good for tasks created over time
   tasks = []
   for item in items:
       task = asyncio.create_task(process(item))
       tasks.append(task)
   ```

3. **Limit concurrent operations**
   ```python
   # Use Semaphore to limit concurrency
   sem = asyncio.Semaphore(10)
   
   async def limited_task(item):
       async with sem:
           return await process(item)
   ```

### Real-World Example
```python
import asyncio
import aiohttp

async def fetch_url(session, url):
    """Fetch a single URL"""
    try:
        async with session.get(url) as response:
            return await response.text()
    except Exception as e:
        return f"Error fetching {url}: {e}"

async def fetch_all_urls(urls):
    """Fetch multiple URLs concurrently"""
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

# Usage
urls = ["http://example.com", "http://google.com"]
results = asyncio.run(fetch_all_urls(urls))
```

### Quick Conversion Guide

| Synchronous | Asynchronous |
|-------------|--------------|
| `def function():` | `async def function():` |
| `time.sleep(1)` | `await asyncio.sleep(1)` |
| `result = function()` | `result = await function()` |
| `for item in items: process(item)` | `await asyncio.gather(*[process(item) for item in items])` |

### Testing Async Code
```python
import pytest
import asyncio

@pytest.mark.asyncio
async def test_async_function():
    result = await my_async_function()
    assert result == expected_value

# Or using unittest
import unittest

class TestAsync(unittest.IsolatedAsyncioTestCase):
    async def test_something(self):
        result = await async_operation()
        self.assertEqual(result, expected)
```

---

## 📚 Additional Resources

- [Official asyncio documentation](https://docs.python.org/3/library/asyncio.html)
- [Real Python Async IO Tutorial](https://realpython.com/async-io-python/)
- [Python asyncio by Example](https://www.pythonsheets.com/notes/python-asyncio.html)

---

**Happy Async Coding! 🚀**