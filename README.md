# Django Product CRUD API

Simple Django REST Framework API for managing products with Git Actions CI.

## Features
- Product CRUD operations
- Function-based views with `@api_view`
- CI/CD with GitHub Actions

## Setup

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd django-product-crud-api-git-action-CI
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment:**
   Create a `.env` file in the root directory:
   ```env
   DEBUG=True
   SECRET_KEY=your-secret-key
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

5. **Run Migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Run Server:**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

- `GET /api/products/` - List all products
- `POST /api/products/` - Create a new product
- `GET /api/products/<id>/` - Retrieve a product
- `PUT /api/products/<id>/` - Update a product
- `DELETE /api/products/<id>/` - Delete a product
