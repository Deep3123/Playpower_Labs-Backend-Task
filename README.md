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

### 6. Run the Development Server
To start the Django development server and run the application locally:

```bash
python manage.py runserver
```

This will start the server, and you can access the application in your browser by navigating to `http://127.0.0.1:8000/`. If you created a superuser, you can log into the Django Admin at `http://127.0.0.1:8000/admin/`.

# API Endpoints

### 1. User Registration (Sign Up)
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

### 2. User Login (JWT Token Generation)
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

### 3. Create a Quiz (Admin/Authenticated User)
- **Endpoint**: `POST /api/create-quiz/`
- **Request Body**:
    ```json
    { 
        "subject": "General Knowledge", 
    }
    ```
- **Response**:
    ```json
    {
    "message": "Quiz created successfully",
    "quiz": {
        "id": 24,
        "subject": "General Knowledge",
        "grade_level": null,
        "question_data": [
            {
                "question_text": "What is the name of the largest moon of Saturn, known for its complex geological features, including cryovolcanism and a subsurface ocean?\n\nOption 1: Titan\nOption 2: Rhea\nOption 3: Iapetus\nOption 4: Enceladus\n\nCorrect Option: Option 1"
            },
            {
                "question_text": "What year did the iconic board game \"Monopoly\" first launch in its current form, featuring the familiar properties and game pieces?\n\nOption 1: 1923\nOption 2: 1935\nOption 3: 1903\nOption 4: 1910\n\nCorrect Option: Option 2"
            },
            {
                "question_text": "What is the name of the longest river in the world that entirely flows within a single country?\n\nOption 1:  Amazon River\nOption 2: Nile River\nOption 3: Yangtze River\nOption 4: Mississippi River\n\nCorrect Option: Option 3 (Yangtze River)"
            },
            {
                "question_text": "What year did the first successful human-powered flight take place, officially recognized by the Fédération Aéronautique Internationale?\n\nOption 1: 1903\nOption 2: 1910\nOption 3: 1896\nOption 4: 1921\n\nCorrect Option: Option 1"
            },
            {
                "question_text": "Which of these countries is landlocked and does not border the Caspian Sea?\n\nOption 1: Kazakhstan\nOption 2: Uzbekistan\nOption 3: Kyrgyzstan\nOption 4: Tajikistan\n\nCorrect Option: Option 3"
            }
        ],
        "created_at": "2024-12-17T14:29:05.803931Z",
        "updated_at": "2024-12-17T14:29:12.053820Z"
       }
   }
    ```

### 4. Generate Hint for a Question
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

### 5. Generate Question for a Student
- **Endpoint**: `POST /api/generate-question/`
- **Request Body**:
    ```json
    { 
        "text": "create question for standard-5 student mathematics."
    }
    ```
- **Response**:
    ```json
    { 
        "generated_question": {
            "question_text": "Here are some math questions suitable for a standard 5 (around 10-11 year old) student, categorized by topic:\n\n**Numbers and Operations:**\n\n1. **Addition and Subtraction:** A farmer has 345 apple trees and 287 pear trees. How many trees does the farmer have in total?  If he sells 150 apple trees, how many apple trees are left?\n\n2. **Multiplication and Division:**  A box contains 24 pencils.  If there are 15 boxes, how many pencils are there in total? If these pencils are divided equally among 6 students, how many pencils does each student get?\n\n3. **Fractions:**  What is 2/3 of 27?  Add 1/4 and 3/8.  Subtract 5/6 from 1.\n\n4. **Decimals:**  Add 3.45 and 2.7. Subtract 1.8 from 5.23. Multiply 2.5 by 4.\n\n5. **Order of Operations (BODMAS/PEMDAS):** Solve: 12 + 6 ÷ 2 × 3 - 4\n\n\n**Geometry and Measurement:**\n\n6. **Perimeter:** A rectangle has a length of 12cm and a width of 5cm. What is its perimeter?\n\n7. **Area:** A square has sides of 8cm. What is its area?\n\n8. **Volume:** A rectangular prism has a length of 10cm, a width of 5cm, and a height of 3cm. What is its volume?\n\n9. **Angles:** What type of angle is an angle measuring 110 degrees? (acute, obtuse, right, reflex)\n\n10. **Time:** A movie starts at 7:15 pm and lasts for 2 hours and 30 minutes. What time does the movie end?\n\n\n**Problem Solving:**\n\n11.  Sarah has 3 times as many marbles as Tom. If Tom has 15 marbles, how many marbles does Sarah have?\n\n12. A bus has 40 seats. If 27 people are already on the bus, how many more people can get on?\n\n13.  A pizza is cut into 8 slices. If you eat 3 slices, what fraction of the pizza have you eaten?\n\n\n**Remember to adjust the difficulty based on the specific curriculum and the students' abilities.**  These are examples, and you can modify numbers and contexts to create more questions. You can also add word problems that require multiple steps to solve."
        }
    }

# Testing the APIs in Postman

1. **Open Postman**.
2. **Create a New Request**:
    - Choose `POST` as the HTTP method.
    - Enter the API endpoint (e.g., `http://localhost:8000/api/register/`).
    - In the "Body" tab, select `raw` and `JSON` format.
    - Add the request data in JSON format (refer to each endpoint for the expected data).
3. **Authentication**:
    - For endpoints that require authentication (like Create Quiz, Submit Quiz), use the token obtained from the Login endpoint:
        - In Postman, go to the "Headers" tab.
        - Add a new key: `Authorization`.
        - Set the value to `Bearer <access_token>`, where `<access_token>` is the token obtained from the Login API.
4. **Send the Request**:
    - Click on the "Send" button.
    - View the response from the API in the "Response" section.
5. **Check Responses**:
    - Verify that the responses are as expected (check status codes, messages, and response data).

# Additional Notes

- **Caching**: The API uses caching to store quizzes for 1 hour after creation to optimize performance.
- **Error Handling**: If there are any issues such as missing fields or invalid credentials, the API will return an appropriate error message.
