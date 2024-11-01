# My Portfolio and CV

Welcome to my personal portfolio and CV project built using Django! This project showcases my professional experiences, educational background, projects, and skills. 

This project is a work in progress and is set up in a way to help me develop it further.

## Features

- **Multi-Page Portfolio**: Navigate through different sections showcasing my work and experiences.
- **Dynamic Content**: Data is pulled from a database, allowing for easy updates via the Django admin interface.
- **Responsive Design**: The layout adapts to different screen sizes for optimal viewing on mobile and desktop devices.

## Technologies Used

- **Django**: A high-level Python web framework for rapid development.
- **SQLite**: A lightweight database to store all portfolio content.
- **HTML/CSS**: For structuring and styling the pages.
- **Bootstrap**: For responsive design (if applicable).

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Django 5.x
- A virtual environment (recommended)

### Installation

1. Clone the repository:
   ```python
   git clone https://github.com/codymathews1995/mycv.git
   cd mycv
    ```

2. Create virtual environment:
    ```python
    python -m venv .venv
    .venv\Scripts\activate
    ```

3. Install the requirements:
    ```python
    pip install -r requirements.txt
    ```

4. Run database migrations:
    ```python
    python manage.py migrate
    ```

5. Create a superuser to access the admin interface
    ```python
    python manage.py createsuperuser
    ```

6. Run development server:
    ```python
    python manage.py runserver
    ```

7. Visit `http://127.0.0.1:8000/` in your browser to view the portfolio.

## Admin Access

To manage portfolio content, you can access the Django admin panel by visiting http://127.0.0.1:8000/admin/ and logging in with the superuser credentials you created.

## Adding Content

You can add professional experiences, educational background, projects, and skills through the Django admin interface. Make sure to upload any images you wish to use in the media folder.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Cody Mathews - [My GitHub Profile](https://github.com/codymathews1995)

## Acknowledgements
Thanks to Django and the open-source community for providing such powerful tools.