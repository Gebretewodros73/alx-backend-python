# Asynchronous Comprehensions and Generators

This directory contains Python scripts demonstrating the use of asynchronous generators and comprehensions.

## Tasks

### 0. Async Generator (Mandatory)
- **File**: 0-async_generator.py
- **Instructions**:
  - Write a coroutine called `async_generator` that takes no arguments.
  - The coroutine will loop 10 times, each time asynchronously waiting for 1 second, then yield a random number between 0 and 10 using the random module.

### 1. Async Comprehensions (Mandatory)
- **File**: 1-async_comprehension.py
- **Instructions**:
  - Import the `async_generator` from the previous task and then write a coroutine called `async_comprehension` that takes no arguments.
  - The coroutine will collect 10 random numbers using an async comprehension over `async_generator`, then return the 10 random numbers.

### 2. Run time for four parallel comprehensions (Mandatory)
- **File**: 2-measure_runtime.py
- **Instructions**:
  - Import `async_comprehension` from the previous file and write a `measure_runtime` coroutine that will execute `async_comprehension` four times in parallel using `asyncio.gather`.
  - `measure_runtime` should measure the total runtime and return it. Notice that the total runtime is roughly 10 seconds.

## Usage

To run the provided examples, you can use the following command for each task:

```bash
./<Task-Number>-main.py
```

## Repository Information

- GitHub repository: [alx-backend-python](./)
- Directory: [0x02-python_async_comprehension](./0x02-python_async_comprehension)

