# Python Generators: Efficient Data Processing with SQL Integration

## About the Project

This project explores advanced usage of **Python generators** to efficiently handle large datasets, process data in batches, and simulate real-world scenarios involving live updates and memory-efficient computations. By leveraging Python’s `yield` keyword, the project demonstrates how to implement generators for iterative, lazy data processing that optimizes resource utilization and enhances performance in data-driven applications.

The tasks guide you through practical use cases such as streaming data from SQL databases, batch processing, paginated lazy loading, and memory-efficient aggregate computations, all within the context of real database-driven workflows.

---

## Project Structure and Tasks

Each task builds on the previous, progressively deepening your understanding of generators and their practical applications.

### 0. Getting Started with Python Generators

* **Objective:** Create a generator to stream rows from an SQL database one at a time.
* **Key Activities:**

  * Set up MySQL database `ALX_prodev` and create the `user_data` table with appropriate schema.
  * Seed the database with sample data from `user_data.csv`.
  * Implement database connection and seeding scripts (`seed.py`).

### 1. Generator to Stream Rows from SQL

* **Objective:** Implement a generator function `stream_users()` to fetch and yield rows one by one from the `user_data` table.
* **Focus:** Efficient row-by-row data access using a single loop and `yield`.

### 2. Batch Processing Large Data

* **Objective:** Create generators to fetch and process data in batches.
* **Tasks:**

  * `stream_users_in_batches(batch_size)` yields batches of users.
  * `batch_processing(batch_size)` filters users over age 25 within each batch.
* **Constraints:** Use no more than three loops and apply generator-based batch processing.

### 3. Lazy Loading Paginated Data

* **Objective:** Simulate paginated data fetching using a generator to lazily load each page on demand.
* **Key Functions:**

  * `paginate_users(page_size, offset)` to fetch data pages.
  * `lazy_paginate(page_size)` generator that yields each page sequentially.
* **Use Case:** Demonstrates efficient pagination for large datasets.

### 4. Memory-Efficient Aggregation with Generators

* **Objective:** Compute aggregate functions (e.g., average age) efficiently using generators without loading the full dataset into memory.
* **Tasks:**

  * Implement `stream_user_ages()` generator to yield user ages.
  * Calculate the average age by iterating over the generator output.
* **Restrictions:** Avoid SQL aggregate functions and limit to two loops.

---

## Usage

Each task includes a main executable script (e.g., `0-main.py`, `1-main.py`, etc.) to demonstrate the generator functionality and outputs sample results.
