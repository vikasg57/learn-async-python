# Exercise Problem Descriptions

## Exercise 1: Coffee Shop Simulator 📍

**File:** `02-exercises/exercise1_coffee_shop/problem.md`

```markdown
# Exercise 1: Coffee Shop Simulator ☕

## Difficulty: Beginner

## Learning Objectives
- Practice basic `async`/`await` syntax
- Use `asyncio.gather()` for concurrent execution
- Understand time measurement in async programs

## Problem Statement
You are building a coffee shop simulation where multiple baristas can prepare different drinks simultaneously. Each drink takes a different amount of time to prepare.

## Requirements

### Functional Requirements
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

### Expected Output
```
Starting to make Espresso...
Starting to make Latte...
Starting to make Cappuccino...
Espresso is ready!
Cappuccino is ready!
Latte is ready!
All drinks prepared in 5.0 seconds
```

### Constraints
- All drinks must be prepared concurrently (not sequentially)
- Total time should be approximately 5 seconds (the longest drink time)
- Use `asyncio.gather()` for concurrent execution

## Hints
- Use `time.time()` to measure total execution time
- Remember to `await` async functions
- `asyncio.gather()` can run multiple coroutines concurrently

## Bonus Challenges
1. Add random preparation times (2-6 seconds per drink)
2. Add a customer name parameter to each drink
3. Implement a queue system for multiple orders

## What You'll Learn
- How async functions can run concurrently
- The difference between sequential and parallel execution
- Basic usage of `asyncio.gather()`
```

---

## Exercise 2: Website Status Checker 🌐

**File:** `02-exercises/exercise2_website_checker/problem.md`

```markdown
# Exercise 2: Website Status Checker 🌐

## Difficulty: Beginner-Intermediate

## Learning Objectives
- Practice async loops
- Implement error handling
- Work with random delays and results
- Process multiple async operations

## Problem Statement
Create a website monitoring system that checks multiple websites' status simultaneously. The checker should simulate network delays and random failures.

## Requirements

### Functional Requirements
1. Create an async function `check_website(url)`:
   - Print "Checking {url}..."
   - Simulate network delay (random 1-3 seconds)
   - Return True (80% probability) or False (20% probability)
   - Print "✅ {url} is online" or "❌ {url} is offline"

2. Create main function `monitor_websites()`:
   - Check 5 websites simultaneously
   - Count online vs offline sites
   - Print summary statistics

### Website List
```python
websites = [
    "google.com",
    "github.com", 
    "stackoverflow.com",
    "python.org",
    "asyncio-docs.com"
]
```

### Expected Output Format
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

## Hints
- Use `random.uniform(1, 3)` for delays
- Use `random.random() < 0.8` for 80% probability
- Store results as tuples: (url, status)
- Use `asyncio.gather()` with return values

## Bonus Challenges
1. Add retry logic for failed checks
2. Implement timeout handling
3. Add response time per website
4. Create a continuous monitoring loop

## What You'll Learn
- Handling multiple async operations
- Working with random delays
- Collecting and processing async results
- Basic error simulation
```

---

## Exercise 3: Download Manager 📥

**File:** `02-exercises/exercise3_download_manager/problem.md`

```markdown
# Exercise 3: Download Manager 📥

## Difficulty: Intermediate

## Learning Objectives
- Compare sequential vs parallel execution
- Show progress for async operations
- Calculate performance improvements
- Work with different file sizes

## Problem Statement
Build a download manager that can download files either sequentially (one after another) or in parallel (all at once). Compare the performance difference.

## Requirements

### Functional Requirements
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

### Test Data
```python
files = [
    ("movie.mp4", 500),      # 5 seconds
    ("music.mp3", 50),       # 0.5 seconds
    ("document.pdf", 10),    # 0.1 seconds
    ("image.jpg", 5),        # 0.05 seconds
    ("archive.zip", 300)     # 3 seconds
]
```

### Expected Output
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

## Hints
- Download time = size_mb / 100
- Use `asyncio.gather()` for parallel downloads
- Track start time with `time.time()`

## Bonus Challenges
1. Add bandwidth limiting
2. Implement pause/resume functionality
3. Add progress bars with percentages
4. Simulate download failures and retries

## What You'll Learn
- Performance benefits of async programming
- Sequential vs concurrent execution
- Progress tracking in async operations
```

---

## Exercise 4: Restaurant Order System 🍽️

**File:** `02-exercises/exercise4_restaurant_system/problem.md`

```markdown
# Exercise 4: Restaurant Order System 🍽️

## Difficulty: Intermediate

## Learning Objectives
- Coordinate multiple async operations
- Handle complex workflows
- Process multiple orders simultaneously
- Work with different timing requirements

## Problem Statement
Create a restaurant order processing system where different kitchen stations prepare parts of an order concurrently. Multiple customer orders should be processed simultaneously.

## Requirements

### Functional Requirements
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

### Test Data
```python
orders = [
    (1, "Alice"),
    (2, "Bob"),
    (3, "Charlie"),
    (4, "Diana")
]
```

### Expected Output
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

## Hints
- Use `random.uniform()` for cooking times
- Use nested `asyncio.gather()` calls
- Track individual order times
- Consider using `asyncio.create_task()` for better control

## Bonus Challenges
1. Add kitchen capacity limits (max 2 main courses at once)
2. Implement order priorities (VIP customers)
3. Add order modifications mid-preparation
4. Create a kitchen load balancer

## What You'll Learn
- Complex async coordination
- Nested concurrent operations
- Real-world async patterns
```

---

## Exercise 5: Task Scheduler with Priorities ⚡

**File:** `02-exercises/exercise5_task_scheduler/problem.md`

```markdown
# Exercise 5: Task Scheduler with Priorities ⚡

## Difficulty: Advanced

## Learning Objectives
- Implement priority-based execution
- Use `asyncio.create_task()`
- Manage task batches
- Track detailed execution metrics

## Problem Statement
Build a task scheduler that processes tasks based on priority levels. High-priority tasks should complete before low-priority tasks begin.

## Requirements

### Functional Requirements
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

### Test Data
```python
# High priority: 3 tasks, 1-2 seconds each
high_priority_tasks = [
    ("HIGH-1", 1.5, "high"),
    ("HIGH-2", 1.8, "high"),
    ("HIGH-3", 1.2, "high")
]

# Low priority: 5 tasks, 2-4 seconds each
low_priority_tasks = [
    ("LOW-1", 2.5, "low"),
    ("LOW-2", 3.0, "low"),
    ("LOW-3", 2.2, "low"),
    ("LOW-4", 3.5, "low"),
    ("LOW-5", 2.8, "low")
]
```

### Expected Output
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

## Hints
- Use separate functions for each priority batch
- Consider using `asyncio.as_completed()` for progress
- Track timing at multiple levels
- Use colored output for better visualization (optional)

## Bonus Challenges
1. Add medium priority level
2. Implement task dependencies
3. Add task cancellation capability
4. Create dynamic priority adjustment
5. Implement task retry on failure

## What You'll Learn
- Advanced task management
- Priority queue concepts in async
- Performance monitoring
- Complex async workflows
```