<div style="display: flex; justify-content: center; align-items: center; height: 100vh; width: 100vw; margin: auto;">
  <img src="https://yosbel.pages.dev/assets/myChat-Bm_YKV5_.jpeg" alt="Chat pic" style="width: 100%; margin: auto;">
</div>


# Django Chat App


## Project Overview

**Django Chat App** is a Django-based chat application designed to facilitate real-time messaging. The project showcases Django's capabilities in handling real-time communication, user authentication, and a user-friendly interface.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Features](#features)
4. [Project Structure](#project-structure)
5. [Contributing](#contributing)
6. [License](#license)
7. [References](#references)

## Installation

### Prerequisites

- Python 3.x
- Django 3.x

### Steps

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yosbelm/mychat.git
    cd mychat
    ```

2. **Create and activate a virtual environment (optional but recommended):**

    ```sh
    virtualenv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Apply database migrations:**

    ```sh
    python manage.py migrate
    ```

5. **Create a superuser (for accessing the admin interface):**

    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

7. **Access the application:**

    Open your web browser and navigate to `http://127.0.0.1:8000`.

## Usage

### Admin Panel

To access the admin panel:

1. Create a superuser:

    ```sh
    python manage.py createsuperuser
    ```

2. Log in to the admin panel at `http://127.0.0.1:8000/admin`.

### Using the Chat App

1. **Register or log in:**
    - Register a new user or log in with an existing account.

2. **Start chatting:**
    - Send and receive messages in real-time.
    - Click on profile pictures to view user descriptions.
    - Monitor unread message counts and see the latest messages in each chat.

## Features

- Simple authentication/login system.
- Automatic sending and receiving of messages.
- Messages displayed in chronological order.
- Unread message count for each chat.
- Display of the last sent message in each chat.
- Brief user descriptions shown upon clicking profile pictures.

## Project Structure

```plaintext
mychat/
│
├── chat/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── consumers.py
│   ├── models.py
│   ├── routing.py
│   ├── tests.py
│   └── views.py
│
├── chat_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3
├── manage.py
└── requirements.txt