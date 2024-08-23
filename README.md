# Resto-Shop-Backend

This project is the backend for a restaurant shop application built using Django. It provides API endpoints for managing and retrieving food item data.

## Table of Contents
- Features
- Tech Stack
- Project Structure
- Setup Instructions
- Running the Application
- API Endpoints
- Future Improvements
- Contributing
- License

### Features
- API endpoint to retrieve a list of food items.
- API endpoint to retrieve details of a specific food item.
- Dummy data for testing and development purposes.
- CORS support to allow cross-origin requests from the frontend.

### Tech Stack
- `Django:` High-level Python web framework for building the backend.
- `Django REST Framework:` Toolkit for building Web APIs.
- ` Python:` Programming language used to build the backend.


## Setup Instructions

### Prerequisites
Ensure you have the following installed:

- Python (v3.8 or later)
- pip (Python package installer)

### Installation
#### Clone the repository:

```bash
git clone https://github.com/chinemeze847/Resto-Shop-Backend.git
cd restaurant-shop-backend

```
#### Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
### Install dependencies:

```bash
pip install -r requirements.txt
```
### Apply migrations:

```bash
python manage.py migrate
```
### Running the Application
Start the development server:

```bash
python manage.py runserver
```
The application will be available at http://127.0.0.1:8000.

## API Endpoints
### List Food Items
- URL: /api/food-items/
- Method: GET
- Description: Retrieves a list of food items.
- Response:
```json
[
  {
    "id": 1,
    "name": "Spaghetti Carbonara",
    "description": "Classic Italian pasta with creamy sauce and pancetta.",
    "price": "$12",
    "image": "https://example.com/spaghetti.jpg"
  },
  ...
]
```
### Food Item Details
- URL: /api/food-items/<id>/
- Method: GET
- Description: Retrieves details of a specific food item.
- Response:

```json
{
  "id": 1,
  "name": "Spaghetti Carbonara",
  "description": "Classic Italian pasta with creamy sauce and pancetta.",
  "price": "$12",
  "image": "https://example.com/spaghetti.jpg",
  "more_details": "Additional information about the dish."
}
```