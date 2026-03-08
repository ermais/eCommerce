# Gebeya eCommerce

A Django-based eCommerce platform with product management and shopping cart functionality.

## Features

- Product catalog with images and specifications
- Shopping cart system
- User authentication
- Product inventory management
- Price and sale price support
- Admin interface for product management

## Tech Stack

- Django 2.1.5
- SQLite database
- Python 3

## Project Structure

```
eCommerce/
├── gebeya/          # Main project settings
├── products/        # Product management app
├── carts/           # Shopping cart functionality
├── templates/       # Global templates
└── warehouse/       # Media storage
```

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install django pillow
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the application at `http://127.0.0.1:8000/`

## Apps

### Products
- Product model with title, description, price, and inventory
- Product specifications
- Product images with automatic upload handling
- Active/inactive product status

### Carts
- Shopping cart management
- Cart items with quantity tracking
- Automatic subtotal calculation
- User-specific carts

## Admin Access

Access the admin panel at `http://127.0.0.1:8000/admin/` using your superuser credentials.

## Security Note

⚠️ **Important**: Change the SECRET_KEY in settings.py before deploying to production and set DEBUG = False.

## License

This project is for educational purposes.
