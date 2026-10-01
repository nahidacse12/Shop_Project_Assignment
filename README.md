# Shop Project - Product REST API

Django + Django REST Framework Product API for the assignment.

## Features

* Product model: id, name, description, price, stock
* SQLite database
* Public `GET /api/products/`
* Token-authenticated `POST /api/products/`
* `IsAuthenticatedOrReadOnly` permission
* Validation for name, price, and stock
* Pagination: 5 products per page
* Products ordered by id
* Token authentication using DRF's built-in TokenAuthentication

## Setup

Create and activate a virtual environment:

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

## Create Test User and Token

Create a test user:

```bash
python manage.py createsuperuser
```

Generate a token:

```bash
python manage.py drf_create_token YOUR_USERNAME
```

The command will return an authentication token.

For POST requests, use this header:

```text
Authorization: Token YOUR_TOKEN
```

Replace `YOUR_TOKEN` with the token generated for your user.

## API Endpoints

### Get Products

```text
GET /api/products/
```

Full URL:

```text
http://127.0.0.1:8000/api/products/
```

This endpoint is public and does not require authentication.

### Add Product

```text
POST /api/products/
```

This endpoint requires authentication.

Example request body:

```json
{
    "name": "Notebook",
    "description": "A notebook with 100 pages.",
    "price": "120.00",
    "stock": 25
}
```

Successful requests return:

```text
201 Created
```

### Page 2

```text
GET /api/products/?page=2
```

The API returns products using pagination, with 5 products per page.

## Validation

The API validates:

* Product name cannot be empty.
* Price must be greater than zero.
* Stock must be a whole number.
* Stock cannot be negative.

Invalid data returns:

```text
400 Bad Request
```

## Authentication

DRF TokenAuthentication is used.

GET requests are available without authentication.

POST requests require a valid token.

Example:

```text
Authorization: Token YOUR_TOKEN
```

A POST request without a valid token is denied.

## Testing with Postman

The API was tested using Postman.

The following tests were completed:

1. View products without a token → `200 OK`
2. Add a valid product with a valid token → `201 Created`
3. Add a product without a token → `401 Unauthorized`
4. Add a product with an empty name → `400 Bad Request`
5. Add a product with price `0.00` → `400 Bad Request`
6. Add a product with negative stock → `400 Bad Request`
7. View page 2 after adding six products → `200 OK`

For POST requests in Postman:

* Select `POST`
* Open `Body`
* Select `raw`
* Select `JSON`
* Enter the product information
* Add the authentication header

## Submission Screenshots

The submission should include screenshots showing:

1. Successful GET request
2. Successful authenticated POST request (`201 Created`)
3. Authentication error (`401 Unauthorized`)
4. Validation error (`400 Bad Request`)
5. Page 2 showing the sixth product

## Security

Do not commit passwords, authentication tokens, or sensitive credentials to GitHub.

The SQLite database file `db.sqlite3` should also not
