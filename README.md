# Django Chat Application

##Project Description
This Django-based chat application offers a simple authentication/login system, automatic sending and receiving of messages, and displays messages sorted by received time. It shows the number of unread messages in chats, the last sent message, and a brief description of each user when their profile picture is clicked. The project is built with Django, utilizing some JavaScript for real-time messaging functionalities, and HTML/CSS for the frontend.

This Django-based chat application offers the following features:
- Simple authentication/login system.
- Automatic sending and receiving of messages.
- Messages displayed in chronological order.
- Unread message count for each chat.
- Display of the last sent message in each chat.
- Brief user descriptions shown upon clicking profile pictures.

## Technologies Used
- Django
- JavaScript (for real-time messaging)
- HTML/CSS

## Installation and Setup

Follow these steps to set up the project on your local machine:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/django-chat-app.git
    cd django-chat-app
    ```

2. **Create and activate a virtual environment (optional but recommended):**
    ```bash
    virtualenv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser (for accessing the admin interface):**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7. **Access the application:**
    Open your web browser and navigate to `http://127.0.0.1:8000`.

## Usage

1. **Register or log in:**
    - Register a new user or log in with an existing account.

2. **Start chatting:**
    - Send and receive messages in real-time.
    - Click on profile pictures to view user descriptions.
    - Monitor unread message counts and see the latest messages in each chat.

## Contributing

Feel free to submit issues and pull requests for improvements or bug fixes. Contributions are welcome!

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
