# TODO List App 📝

A clean, responsive web application built with Django for managing daily tasks, organizing them with custom tags, and
tracking deadlines effectively.

## 🚀 Features

* **Task & Tag CRUD:** Full ability to create, read, update, and delete both tasks and tags via Django Class-Based
  Views.
* **Status Toggling:** Easily switch task status between "Complete" and "Undo" using a secure `POST` method
  architecture.
* **Session Tracking:** Built-in visit counter utilizing Django sessions displayed dynamically on the main dashboard.
* **Live Statistics:** Dynamic counter showing the total number of tasks and tags currently stored in the system.
* **Pagination:** Smooth data navigation with clean pagination (5 items per page) for both task and tag lists.
* **Smart Ordering:** Automated sorting mechanism ensuring incomplete and newest tasks appear first.

## 🛠️ Tech Stack

* **Backend:** Python 3.x, Django 4.x / 5.x
* **Database:** SQLite (Development standard)
* **Frontend:** HTML5, CSS3, Bootstrap 4

## 📊 Database Structure

The database schema consists of two core interconnected models:

* **Tag:** Represents categories (`name` is unique).
* **Task:** Contains `content`, auto-generated creation timestamp (`datetime`), optional `deadline`, completion status (
  `is_done`), and a `ManyToManyField` relation to **Tag**.

## 🔧 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SerhiiAm/todo-list.git
   cd todo-list
   ```

2. **Create and activate virtual environment:**
    ```bash
    python -m venv venv
    source venv/Scripts/activate  # On Windows (Git Bash)
    # Or "source venv/bin/activate" on macOS/Linux
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run migrations & Start server:**
  ```bash
    python manage.py migrate
    python manage.py runserver
  ```
