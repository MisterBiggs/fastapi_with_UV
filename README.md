# FastAPI Project Setup with UV: A Detailed Guide

This document provides a comprehensive guide to setting up a FastAPI project using UV, covering project initialization, dependency management, API endpoint creation, server execution, documentation access, and testing.

## 1. Project Initialization

* **Action:** Create a new project directory.
* **Command:** `uv init .` (Execute this command within the newly created folder).
* **Result:** This command initializes a new Python project using UV. It sets up a basic project structure and generates a `pyproject.toml` file, which is crucial for managing project metadata and dependencies.

## 2. Initial `pyproject.toml` Configuration

* **Content:**
    ```toml
    [project]
    name = "fastapi"
    version = "0.1.0"
    description = "Add your description here"
    readme = "README.md"
    requires-python = ">=3.13"
    dependencies = []
    ```
* **Explanation:**
    * This `pyproject.toml` file serves as the project's configuration hub.
    * It contains essential metadata:
        * `name`: The name of the project.
        * `version`: The project's version number.
        * `description`: A brief description of the project.
        * `readme`: Specifies the file containing the project's README documentation.
        * `requires-python`: Defines the minimum Python version required for the project.
        * `dependencies`: An initially empty list where project dependencies will be specified.

## 3. Creating `main.py`

* **Action:** Create a file named `main.py` within the project directory.
* **Location:** `C:\Users\xeesh\OneDrive\Desktop\Afnan\AI\fastapi_explore\main.py` (or the equivalent path on your system).
* **Purpose:** This file will house the core FastAPI application logic, including API endpoint definitions.

## 4. Adding Project Dependencies

* **Rationale:** The initial `pyproject.toml` only specifies the Python version. To build a functional FastAPI application, we need to add the FastAPI framework, Uvicorn (an ASGI server to run the application), and pytest (for testing).
* **Commands:**
    ```bash
    uv add fastapi "uvicorn[standard]"
    uv add --dev pytest httpx
    ```
* **Effects:**
    * Installs the specified packages and their respective sub-dependencies.
    * Automatically updates the `pyproject.toml` file to reflect these dependencies.
    * Generates a `uv.lock` file, which locks down the exact versions of the installed packages, ensuring consistent builds.
    * Adds testing as development dependencies

## 5. Updated `pyproject.toml` with Dependencies

* **Content:**
    ```toml
    [project]
    name = "fastapi_explore"
    version = "0.1.0"
    description = "Add your description here"
    readme = "README.md"
    requires-python = ">=3.13"
    dependencies = [
        "fastapi>=0.115.12",
        "uvicorn[standard]>=0.34.2",
    ]

    [dependency-groups]
    dev = [
        "httpx>=0.28.1",
        "pytest>=8.3.5",
    ]
    ```
* **Explanation:** The `dependencies` section now lists the required packages, including FastAPI, pytest, and Uvicorn, along with their minimum version requirements.

## 6. Defining API Endpoints in `main.py`

* **Code:**
    ```python
    from fastapi import FastAPI

    app = FastAPI()  # Creating an instance of the FastAPI class

    @app.get("/")  # Decorator to define a GET endpoint at the root path "/"
    def index():
        return {"Hello": "World"}

    @app.get("/piaic/")  # Decorator to define a GET endpoint at "/piaic/"
    def piaic():
        return {"organization": "piaic"}
    ```
* **Explanation:**
    * `FastAPI()`: Creates an instance of the FastAPI class, which serves as the application's core.
    * `@app.get("/")` and `@app.get("/piaic/")`: These are decorators that define GET endpoints. The `@` symbol indicates a decorator, which adds functionality to the following function.
    * `index()` and `piaic()`: These are the functions that handle the logic for each endpoint, returning JSON responses.

## 7. Running the FastAPI Server

* **Command:** `uv run uvicorn main:app --reload`
* **Explanation:**
    * Starts the Uvicorn server, which runs the FastAPI application.
    * `main:app` specifies the `main.py` file and the `app` object within it.
    * `--reload` enables automatic server restarts whenever changes are made to the code, facilitating development.
* **Output:**
    ```
    INFO:     Started server process [10728]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    INFO:     Uvicorn running on [http://127.0.0.1:8000](http://127.0.0.1:8000) (Press CTRL+C to quit)
    ```

## 8. Accessing API Endpoints

* **URLs:**
    * `http://127.0.0.1:8000/`
    * `http://127.0.0.1:8000/piaic/`
    * `http://127.0.0.1:8000/docs`

## 9. API Documentation (Swagger UI)

* **Access:** Open `http://127.0.0.1:8000/docs` in a web browser (Chrome or Edge).
* **Purpose:** FastAPI automatically generates interactive API documentation using Swagger UI, allowing developers to explore and test API endpoints directly.

## 10. Writing and Running Tests

* **Rationale:** Writing tests is essential for ensuring the reliability and correctness of API endpoints.
* **Test File:** Create a file named `test_main.py` in the project directory.
* **Test Functions:** Each test function should begin with `test_` so that pytest can automatically discover them.
* **Execution:**
    * **Command:** `uv run pytest` (Run from the project directory).
    * **Result:** pytest automatically discovers and executes test files, providing feedback on test success or failure. This allows for automated testing of all functions within the project.