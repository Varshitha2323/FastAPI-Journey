# 📚 Day 1: FastAPI Foundations & Data Validation



## 1. Environment & Setup

To start any FastAPI project, you need the core library and an ASGI server (**Uvicorn**).



* **Installation**:

    ```bash

    pip install "fastapi[standard]"

    ```

* **Running the Development Server**:

    ```bash

    python -m uvicorn main:app --reload

    ```

    * `--reload`: Automatically restarts the server whenever you save your code.

* **Interactive Documentation**:

    * **Swagger UI**: `http://127.0.0.1:8000/docs`

    * **ReDoc**: `http://127.0.0.1:8000/redoc`



---



## 2. The Three Pillars of Data Input

FastAPI determines where data comes from based on how you define your function arguments.



| Type | Location | Syntax | Best Use Case |

| :--- | :--- | :--- | :--- |

| **Path Parameter** | Inside the URL path | `/items/{item_id}` | Identifying a specific resource (ID). |

| **Query Parameter** | After the `?` in URL | `/items?limit=10` | Filtering, sorting, or pagination. |

| **Request Body** | Hidden in the request | `item: ItemModel` | Sending complex data (JSON). |







---



## 3. Data Validation with Pydantic

Pydantic allows us to define "Schemas" (templates). FastAPI uses these to validate that incoming data is correct before your code even runs.



### Key Validation Tools:

* **`BaseModel`**: The parent class for all data schemas.

* **`Field`**: Used inside models to set rules (e.g., `gt` for greater than, `min_length` for strings).

* **`Path` / `Query`**: Used in function arguments to add metadata and validation to URL parameters.



```python

from pydantic import BaseModel, Field


class User(BaseModel):

    username: str = Field(..., min_length=3)

    age: int = Field(..., ge=18)  # ge = Greater than or Equal to
```


## 4. Professional Error Handling

Instead of letting Python throw a standard error (which crashes the request), we use HTTPException to return a clean, structured response to the client.



```python

from fastapi import HTTPException



# Example: Checking if an item exists

if item_id not in database:

    raise HTTPException(

        status_code=404, 

        detail="The item you are looking for does not exist."

    )

```

## 5. Lessons Learned & Troubleshooting

The "Required" Path Error: Path parameters cannot have a default value of None. Use ... (Ellipsis) to tell FastAPI the parameter is strictly required.



Typo Alert: The argument is status_code (singular, no 'e' after 'status').



Virtual Environments: Always ensure your .venv is active before installing packages to avoid global version conflicts.


---


##🛠️ Day 1 Project Summary

Successfully built a Library Management API that uses:



GET to fetch all books or a specific book by ID.



POST to add new books with validation logic.



Manual Error Handling to catch invalid IDs.
