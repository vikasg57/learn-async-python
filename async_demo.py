import asyncio
import time


async def task(name, duration):
    print(f"Task {name} starting (will take {duration}s)")
    await asyncio.sleep(duration)
    print(f"Task {name} done!")
    return f"Result from {name}"


async def main():
    print("=== Running tasks sequentially ===")
    start = time.time()

    # Sequential - slow
    result1 = await task("A", 2)
    result2 = await task("B", 2)

    print(f"Sequential took: {time.time() - start:.1f}s\n")

    print("=== Running tasks concurrently ===")
    start = time.time()

    # Concurrent - fast
    results = await asyncio.gather(
        task("C", 2),
        task("D", 2)
    )

    print(f"Concurrent took: {time.time() - start:.1f}s")
    print(f"Results: {results}")


# Run the program
if __name__ == "__main__":
    asyncio.run(main())