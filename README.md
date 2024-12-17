# AI Quizzer API

The **AI Quizzer API** is a Django-based API that allows users to register, log in, create quizzes, generate questions, submit answers, and retrieve AI-powered hints. Built using **Django REST Framework** and **JWT authentication**, this API enables quiz management and AI-driven content generation.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- Django 3.x or higher
- Django REST Framework
- djangorestframework-simplejwt
- google-generativeai
- PostgreSQL or another database setup
- Postman (for API testing)

## Setup Steps

### 1. Clone the Project
Clone the repository to your local machine:

```bash
git clone https://github.com/Deep3123/Playpower_Labs-Backend-Task.git
```

### 2. Install Dependencies
Navigate to your project directory and install the required packages from the `requirements.txt` file:

```bash
cd ai_quizzer
pip install -r requirements.txt
```

### 3. Setup Database
Configure your database settings in `settings.py`. If you're using DBSQLite, the default database configurations will work, but you may need to adjust for a different database.

### 4. Apply Migrations
Run the migrations to set up the database schema:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (Optional)
If you want to access the Django Admin interface, create a superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to create the admin account.

# API Endpoints

## 1. User Registration (Sign Up)
- **Endpoint**: `POST /api/register/`
- **Request Body**:
    ```json
    { 
        "username": "user_name", 
        "password": "password" 
    }
    ```
- **Response**:
    ```json
    { 
        "message": "User created successfully", 
        "username": "user_name" 
    }
    ```

## 2. User Login (JWT Token Generation)
- **Endpoint**: `POST /api/login/`
- **Request Body**:
    ```json
    { 
        "username": "user_name", 
        "password": "password" 
    }
    ```
- **Response**:
    ```json
    { 
        "token": "<access_token>", 
        "refresh": "<refresh_token>" 
    }
    ```

## 3. Create a Quiz (Admin/Authenticated User)
- **Endpoint**: `POST /api/create_quiz/`
- **Request Body**:
    ```json
    { 
        "subject": "General Knowledge", 
        "quiz_title": "Sample Quiz", 
        "duration": 30 
    }
    ```
- **Response**:
    ```json
    { 
        "message": "Quiz created successfully", 
        "quiz": { 
            "subject": "General Knowledge", 
            "quiz_title": "Sample Quiz", 
            "duration": 30 
        } 
    }
    ```

## 4. Generate Hint for a Question
- **Endpoint**: `POST /api/generate_hint/`
- **Request Body**:
    ```json
    { 
        "question_text": "What is the capital of France?" 
    }
    ```
- **Response**:
    ```json
    { 
        "hint": "The capital of France is known for the Eiffel Tower." 
    }
    ```

# Testing the APIs in Postman

1. **Open Postman**.
2. **Create a New Request**:
    - Choose `POST` as the HTTP method.
    - Enter the API endpoint (e.g., `http://localhost:8000/api/register/`).
    - In the "Body" tab, select `raw` and `JSON` format.
    - Add the request data in JSON format (refer to each endpoint for the expected data).
3. **Authentication**:
    - For endpoints that require authentication (like Create Quiz, Submit Quiz), use the token obtained from the Login endpoint:
        - In Postman, go to the "Authorization" tab.
        - Select "Bearer Token" and paste the JWT access token.
4. **Send the Request**:
    - Click on the "Send" button.
    - View the response from the API in the "Response" section.
5. **Check Responses**:
    - Verify that the responses are as expected (check status codes, messages, and response data).

# Additional Notes

- **Caching**: The API uses caching to store quizzes for 1 hour after creation to optimize performance.
- **Error Handling**: If there are any issues such as missing fields or invalid credentials, the API will return an appropriate error message.
