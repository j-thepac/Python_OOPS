from concurrent.futures import ThreadPoolExecutor
def task(n):
    return n * n
# Use ThreadPoolExecutor to run tasks concurrently
with ThreadPoolExecutor() as executor:
    results = list(executor.map(task, range(5)))
print(results)  # Output: [0, 1, 4, 9, 16]
# Advantages: Simplifies thread and process management, easy to use.