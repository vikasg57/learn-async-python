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

# Advanced Async Python Learning Path 🚀

## 📊 Your Current Level
✅ Basic async/await syntax
✅ asyncio.gather() and create_task()
✅ Concurrent vs sequential execution
✅ Basic error handling
✅ Priority-based processing

## 🎯 Advanced Learning Path

### Phase 1: Advanced Core Concepts (Week 1-2)

#### Exercise 6: Async Queue System 📬
Build a producer-consumer system with async queues.

```python
"""
Requirements:
1. Create multiple producers adding tasks to a queue
2. Create multiple consumers processing tasks from the queue
3. Implement queue size limits
4. Add task priorities in queue
5. Track metrics (throughput, latency)
"""

import asyncio
import random
import time
from typing import Any, Dict

class AsyncTaskQueue:
    def __init__(self, max_size: int = 10, num_workers: int = 3):
        self.queue = asyncio.Queue(maxsize=max_size)
        self.workers = num_workers
        self.metrics = {
            'processed': 0,
            'failed': 0,
            'total_time': 0
        }
    
    async def producer(self, producer_id: int, num_tasks: int):
        """Add tasks to queue"""
        # Your implementation here
        pass
    
    async def consumer(self, worker_id: int):
        """Process tasks from queue"""
        # Your implementation here
        pass
    
    async def run(self):
        """Coordinate producers and consumers"""
        # Your implementation here
        pass

# Goal: Process 100 tasks with 5 producers and 3 consumers
# Track: Average processing time, queue wait time, throughput
```

#### Exercise 7: Rate Limiter & Throttling 🚦
Implement an async rate limiter using token bucket algorithm.

```python
"""
Requirements:
1. Limit API calls to X requests per second
2. Implement token bucket algorithm
3. Handle burst traffic
4. Add retry logic with exponential backoff
5. Support multiple rate limit tiers
"""

class AsyncRateLimiter:
    def __init__(self, rate: int, per: float = 1.0, burst: int = None):
        """
        rate: number of requests
        per: time period in seconds
        burst: maximum burst size
        """
        # Your implementation
        pass
    
    async def acquire(self):
        """Wait if necessary to stay within rate limit"""
        pass
    
    async def __aenter__(self):
        await self.acquire()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass

# Usage example:
# limiter = AsyncRateLimiter(rate=10, per=1.0)  # 10 requests per second
# async with limiter:
#     await make_api_call()
```

#### Exercise 8: Async Context Manager & Resources 🔒
Create an async database connection pool.

```python
"""
Requirements:
1. Implement async context manager for connections
2. Create connection pool with size limits
3. Handle connection recycling
4. Add health checks for connections
5. Implement connection timeout and retry
"""

class AsyncConnectionPool:
    async def __aenter__(self):
        """Acquire connection from pool"""
        pass
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Return connection to pool"""
        pass
    
    async def execute(self, query: str):
        """Execute query with automatic connection management"""
        pass

# Goal: Handle 1000 concurrent database operations efficiently
```

---

### Phase 2: Real-World Patterns (Week 3-4)

#### Exercise 9: Web Scraper with Concurrency Control 🕷️
Build an async web scraper with politeness policies.

```python
"""
Requirements:
1. Scrape multiple websites concurrently
2. Respect robots.txt
3. Implement per-domain rate limiting
4. Handle retries and failures gracefully
5. Save results to database asynchronously
6. Monitor progress with live dashboard
"""

import aiohttp
import asyncio
from typing import List, Dict

class AsyncWebScraper:
    def __init__(self, max_concurrent: int = 10, delay_per_domain: float = 1.0):
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self.domain_locks = {}  # Per-domain rate limiting
        self.session = None
        
    async def fetch_url(self, url: str) -> str:
        """Fetch single URL with rate limiting"""
        pass
    
    async def scrape_website(self, base_url: str, max_pages: int = 100):
        """Scrape entire website respecting limits"""
        pass

# Goal: Scrape 1000 pages from 10 different domains efficiently
```

#### Exercise 10: Async Microservice Orchestrator 🎭
Build a system that coordinates multiple microservices.

```python
"""
Requirements:
1. Call multiple services in parallel
2. Implement circuit breaker pattern
3. Add request caching
4. Handle partial failures gracefully
5. Implement timeout and retry strategies
6. Add distributed tracing
"""

class ServiceOrchestrator:
    async def get_user_dashboard(self, user_id: int):
        """
        Coordinate calls to:
        - User service
        - Orders service
        - Recommendations service
        - Notifications service
        
        Handle failures gracefully with fallbacks
        """
        pass

# Goal: Reduce latency from 2s (sequential) to 500ms (parallel)
```

#### Exercise 11: Real-time Data Pipeline 📊
Build an async ETL pipeline for streaming data.

```python
"""
Requirements:
1. Read from multiple data sources concurrently
2. Transform data in parallel
3. Write to multiple destinations
4. Handle backpressure
5. Implement checkpointing for recovery
6. Monitor pipeline health
"""

class AsyncDataPipeline:
    async def extract(self, source: str) -> AsyncIterator[Dict]:
        """Extract data from source"""
        pass
    
    async def transform(self, data: Dict) -> Dict:
        """Transform data"""
        pass
    
    async def load(self, data: Dict, destination: str):
        """Load data to destination"""
        pass
    
    async def run(self):
        """Run the complete pipeline"""
        pass

# Goal: Process 100,000 records per minute
```

---

### Phase 3: Advanced Patterns (Week 5-6)

#### Exercise 12: Distributed Task Queue 🌐
Build a Redis-backed distributed task queue.

```python
"""
Requirements:
1. Distribute tasks across multiple workers
2. Implement task persistence with Redis
3. Add task scheduling (run at specific time)
4. Support task dependencies
5. Implement dead letter queue
6. Add monitoring and metrics
"""

class DistributedTaskQueue:
    def __init__(self, redis_url: str):
        pass
    
    async def enqueue(self, task: Dict, priority: int = 0, delay: int = 0):
        """Add task to queue"""
        pass
    
    async def worker(self, worker_id: str):
        """Worker that processes tasks"""
        pass

# Goal: Handle 10,000 tasks/second across 5 workers
```

#### Exercise 13: WebSocket Server with Pub/Sub 💬
Build a real-time chat server using WebSockets.

```python
"""
Requirements:
1. Handle 1000+ concurrent WebSocket connections
2. Implement pub/sub for rooms
3. Add message history
4. Implement presence (who's online)
5. Add rate limiting per user
6. Support reconnection with message recovery
"""

class AsyncChatServer:
    def __init__(self):
        self.connections = {}
        self.rooms = {}
    
    async def handle_connection(self, websocket, path):
        """Handle new WebSocket connection"""
        pass
    
    async def broadcast_to_room(self, room_id: str, message: Dict):
        """Send message to all users in room"""
        pass

# Goal: Support 1000 concurrent users with <100ms message latency
```

---

### Phase 4: Performance & Optimization (Week 7-8)

#### Exercise 14: Async Performance Profiler 📈
Build a tool to profile async code performance.

```python
"""
Requirements:
1. Track task execution time
2. Monitor event loop lag
3. Detect blocking operations
4. Visualize concurrent task execution
5. Identify bottlenecks
6. Generate performance reports
"""

class AsyncProfiler:
    def __init__(self):
        self.metrics = []
    
    async def profile(self, coro):
        """Profile a coroutine"""
        pass
    
    def generate_report(self):
        """Generate performance report"""
        pass
```

#### Exercise 15: Async Cache with TTL 💾
Implement an efficient async cache with various eviction policies.

```python
"""
Requirements:
1. Implement LRU, LFU, and TTL eviction
2. Support async cache warming
3. Add cache statistics
4. Implement distributed caching
5. Handle cache stampede
6. Add cache invalidation patterns
"""

class AsyncCache:
    def __init__(self, max_size: int = 1000, ttl: int = 300):
        pass
    
    async def get(self, key: str, factory=None):
        """Get from cache or compute"""
        pass
    
    async def invalidate_pattern(self, pattern: str):
        """Invalidate keys matching pattern"""
        pass
```

---

## 🎓 Advanced Concepts to Master

### 1. **Async Generators & Iterators**
```python
async def paginated_fetch(url: str, total_pages: int):
    """Async generator for pagination"""
    for page in range(1, total_pages + 1):
        data = await fetch_page(url, page)
        yield data

# Usage
async for page_data in paginated_fetch(url, 100):
    await process_page(page_data)
```

### 2. **Async Comprehensions**
```python
# Async list comprehension
results = [await process(item) async for item in async_iterator()]

# Async dict comprehension
data = {k: await fetch(k) async for k in keys}
```

### 3. **AsyncIO Streams**
```python
async def handle_client(reader, writer):
    """Handle TCP client connection"""
    data = await reader.read(1024)
    response = await process_request(data)
    writer.write(response)
    await writer.drain()
    writer.close()
```

### 4. **Synchronization Primitives**
```python
# Lock
lock = asyncio.Lock()
async with lock:
    # Critical section
    pass

# Semaphore
sem = asyncio.Semaphore(10)
async with sem:
    # Limited concurrency
    pass

# Event
event = asyncio.Event()
await event.wait()  # Wait for event
event.set()  # Trigger event
```

### 5. **Error Handling Patterns**
```python
# Supervisor pattern
async def supervisor(coro, max_retries=3):
    for attempt in range(max_retries):
        try:
            return await coro
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            await asyncio.sleep(2 ** attempt)

# Circuit breaker pattern
class CircuitBreaker:
    def __init__(self, failure_threshold=5, timeout=60):
        self.failures = 0
        self.threshold = failure_threshold
        self.timeout = timeout
        self.last_failure_time = None
        self.state = "closed"  # closed, open, half_open
```

---

## 📚 Project Ideas

### 1. **Async Web Framework** (2 weeks)
Build a mini async web framework like FastAPI:
- Routing system
- Middleware support
- Dependency injection
- Request validation
- WebSocket support

### 2. **Distributed Web Crawler** (3 weeks)
Build a production-grade web crawler:
- URL frontier management
- Duplicate detection
- Politeness policies
- Distributed crawling
- Data extraction pipeline

### 3. **Real-time Analytics Engine** (3 weeks)
Build a streaming analytics system:
- Ingest data from multiple sources
- Real-time aggregations
- Time-window operations
- Dashboard with WebSockets
- Alerting system

### 4. **Async Game Server** (2 weeks)
Build a multiplayer game server:
- Handle 1000+ concurrent players
- Real-time state synchronization
- Match-making system
- Leaderboards
- Anti-cheat mechanisms

---

## 📖 Resources for Deep Learning

### Books
1. **"Using Asyncio in Python"** by Caleb Hattingh
2. **"High Performance Python"** by Gorelick & Ozsvald
3. **"Architecture Patterns with Python"** by Percival & Gregory

### Online Courses
1. **Python Concurrency** on Real Python
2. **Async Techniques and Examples** on Python docs
3. **Building Async APIs** tutorials

### Libraries to Explore
```python
# Web & APIs
pip install aiohttp fastapi httpx

# Databases
pip install asyncpg aiomysql motor aioredis

# Message Queues
pip install aio-pika aiokafka

# Utilities
pip install aiofiles aiopath aiodns

# Testing
pip install pytest-asyncio aioresponses
```

### Code to Study
1. **FastAPI source code** - Modern async patterns
2. **aiohttp source code** - Low-level async networking
3. **Starlette source code** - ASGI framework patterns
4. **Uvicorn source code** - ASGI server implementation

---

## 🎯 Learning Strategy

### Week 1-2: Advanced Core
- Complete exercises 6-8
- Study async context managers
- Learn about event loop internals

### Week 3-4: Real-World Patterns
- Complete exercises 9-11
- Build a small API with FastAPI
- Practice with real APIs using aiohttp

### Week 5-6: Distributed Systems
- Complete exercises 12-13
- Learn about message queues
- Study distributed patterns

### Week 7-8: Optimization
- Complete exercises 14-15
- Profile your code
- Optimize bottlenecks

### Week 9-12: Big Project
- Choose one major project
- Apply all learned concepts
- Deploy to production

---

## 🏆 Mastery Checklist

- [ ] Can build async APIs handling 10K+ req/sec
- [ ] Understand event loop internals
- [ ] Can debug async code effectively
- [ ] Know when NOT to use async
- [ ] Can profile and optimize async code
- [ ] Understand backpressure and flow control
- [ ] Can implement custom async protocols
- [ ] Can build distributed async systems
- [ ] Know multiple async patterns by heart
- [ ] Can teach async concepts to others

---

## 💡 Pro Tips

1. **Not everything needs to be async** - CPU-bound tasks don't benefit
2. **Beware of blocking operations** - One blocking call ruins concurrency
3. **Use connection pooling** - Don't create connections per request
4. **Monitor your event loop** - Watch for lag and blocking
5. **Test concurrent scenarios** - Race conditions are tricky
6. **Use structured concurrency** - TaskGroups in Python 3.11+
7. **Profile before optimizing** - Measure, don't guess
8. **Handle backpressure** - Don't overwhelm downstream services

---

## 🚀 Next Immediate Steps

1. **Pick Exercise 6** (Async Queue System) and implement it
2. **Install aiohttp**: `pip install aiohttp` and build a simple client
3. **Read FastAPI tutorial**: Understand modern async patterns
4. **Join Python Discord**: Async channel for discussions
5. **Build something real**: Apply concepts to actual problems

Remember: The key to mastery is **building real projects** that solve actual problems. Each exercise above is derived from real-world scenarios I've encountered in production systems.

Good luck on your journey to async mastery! 🎉