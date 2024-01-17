# Async IO in Python
# Asynchronous I/O, or async for short, is a programming pattern that allows for high-performance I/O operations in a concurrent and non-blocking manner. In Python, async programming is achieved through the use of the asyncio module and asynchronous functions.

# Syntax
# Here is the basic syntax for creating an asynchronous function in Python:


# Explain
import asyncio
async def my_async_function():
    # asynchronous code here
    await asyncio.sleep(1)
    return "Hello, Async World!"
async def main():
    result = await my_async_function()
    print(result)
asyncio.run(main())