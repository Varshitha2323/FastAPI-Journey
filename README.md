# 🚀 My FastAPI Learning Journey

Welcome to my FastAPI documentation and project repository! This project tracks my progress from a beginner to an advanced API developer. Each folder represents a day of learning with notes and a mini-project.

## 📅 Roadmap

| Day | Topic | Status | Key Learning |
| :--- | :--- | :--- | :--- |
| **Day 01** | Foundations & CRUD | ✅ Completed | Path/Query Params, Pydantic, & Error Handling |
| **Day 02** | Databases (SQL) | ⏳ Next Up | SQLAlchemy, SQLite, and Migrations |
| **Day 03** | Relational Data | ⬜ Planned | One-to-Many and Many-to-Many Relationships |
| **Day 04** | Security & Auth | ⬜ Planned | JWT Tokens & Password Hashing |

---

## 🛠️ Day 01: The Foundations

In this section, I learned how to set up a FastAPI environment and create a basic library management system.

### Key Concepts Covered:
* **Type Hinting**: Using Python types to validate incoming data automatically.
* **Pydantic Models**: Creating `BaseModel` classes to structure request bodies.
* **Status Codes**: Using `HTTPException` to return proper `404` (Not Found) or `400` (Bad Request) responses.
* **Automatic Docs**: Utilizing `/docs` (Swagger UI) for interactive testing.

### 📖 Mini-Project: Simple Library API
A functional API that manages a dictionary-based database of books.
* **Location**: `Day-01-Basics/mini_project/main.py`
* **Features**:
  * Get all books.
  * Search for a specific book by ID.
  * Add a new book with validation (Title length, Page count).

---

## 💻 How to Run This Project

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/FastAPI-Journey.git](https://github.com/YOUR_USERNAME/FastAPI-Journey.git) ```

 2.**Create a Virtual Environment**:
   python -m venv .venv 
   source .venv/Scripts/activate  # For Windows

 3.**Install Dependencies**:
   pip install fastapi

 4.**Run the server**:
   python -m uvicorn main:app --reload
