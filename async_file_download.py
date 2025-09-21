import asyncio
import time


async def download_file(filename, size_mb):
    """Download with progress updates"""
    print(f"Downloading {filename} ({size_mb}MB): ", end = "")

    chunks = 10  # Divide download into 10 chunks
    chunk_time = (size_mb / 100) / chunks

    start = time.time()
    for i in range(chunks):
        await asyncio.sleep(chunk_time)
        print("■", end ="", flush=True)

    done_time = time.time() - start
    print(f" ✓ {done_time:.2f}s")
    return filename, size_mb, done_time


async def sequential_download(files):
    """Download files one by one"""
    print("\n=== Sequential Download ===")
    start = time.time()

    # Your code here
    results = []
    for file, size in files:
        result = await download_file(file, size)
        results.append(result)

    total_time = time.time() - start
    print(f"Sequential total: {total_time:.2f} seconds")

    return total_time, results


async def parallel_download(files):
    """Download files simultaneously"""
    print("\n=== Parallel Download ===")
    start = time.time()
    # Your code here
    tasks = [download_file(file, size) for file, size in files]
    results = await asyncio.gather(*tasks)
    total_time = time.time() - start
    print(f"Parallel total: {total_time:.2f} seconds")
    return total_time, results


async def main():
    files = [
        ("movie.mp4", 500),
        ("music.mp3", 50),
        ("document.pdf", 10),
        ("image.jpg", 5),
        ("archive.zip", 300)
    ]

    # Run both methods and compare times
    seq_time, _ = await sequential_download(files)
    par_time, _ = await parallel_download(files)

    print(f"\n=== Performance Summary ===")
    print(f"Sequential: {seq_time:.2f} seconds")
    print(f"Parallel: {par_time:.2f} seconds")
    print(f"Speed improvement: {seq_time / par_time:.2f}x faster")


asyncio.run(main())
