# Task Manager Application

This is a simple Django-based Task Manager application that allows users to create, read, update, and delete tasks. It includes a RESTful API for managing tasks and a basic HTML frontend for interacting with the API.


## Features

- Create, Read, Update, and Delete tasks.
- RESTful API for task management.
- Simple HTML frontend for task interaction.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6+
- Django
- Django REST framework

## Getting Started

1. Clone the repository:

   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project directory:

   ```bash
   cd Task
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

4. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Apply migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Run the Django development server:

   ```bash
   python manage.py runserver
   ```

7. Access the application at [http://localhost:8000](http://localhost:8000).

## API Endpoints

- `GET /taskapp/tasks/`: Get a list of all tasks.
- `POST /taskapp/tasks/`: Create a new task.
- `GET /taskapp/tasks/{task_id}/`: Get details of a specific task.
- `PUT /taskapp/tasks/{task_id}/`: Update a specific task.
- `DELETE /taskapp/tasks/{task_id}/`: Delete a specific task.

## Frontend

The application includes a simple HTML frontend for task management. You can access it by opening [http://localhost:8000](http://localhost:8000) in your web browser. Use the form to create new tasks and view, update, or delete existing tasks.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Create a pull request to the original repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to replace `<repository_url>` with the actual URL of your Git repository. Customize this README to provide specific instructions and information about your project.
