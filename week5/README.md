
---

# Loan Management API

## Overview
This API allows managing loan records. You can create, retrieve, update, and delete loans. It is built using Django and Django Rest Framework.

---

## Base URL
```
http://127.0.0.1:8000/api
```

---

## Endpoints

### 1. **GET /loans**

Retrieve all loan records.

- **Request:**
  - Method: `GET`
  - URL: `/loans`
  
- **Response:**
  - Status: `200 OK`
  - Body:
  ```json
  [
    {
      "id": 1,
      "name": "Personal Loan",
      "amount": 5000.0,
      "date": "2025-01-01",
      "reason": "Home renovation"
    },
    {
      "id": 2,
      "name": "Car Loan",
      "amount": 20000.0,
      "date": "2024-12-01",
      "reason": "Purchase of new car"
    }
  ]
  ```

---

### 2. **GET /loans/{id}**

Retrieve a specific loan record by ID.

- **Request:**
  - Method: `GET`
  - URL: `/loans/{id}`
  
- **Response:**
  - Status: `200 OK`
  - Body:
  ```json
  {
    "id": 1,
    "name": "Personal Loan",
    "amount": 5000.0,
    "date": "2025-01-01",
    "reason": "Home renovation"
  }
  ```

---

### 3. **POST /loans**

Create a new loan record.

- **Request:**
  - Method: `POST`
  - URL: `/loans`
  - Body:
  ```json
  {
    "name": "Home Loan",
    "amount": 30000.0,
    "date": "2025-03-01",
    "reason": "Buying a house"
  }
  ```
  
- **Response:**
  - Status: `201 Created`
  - Body:
  ```json
  {
    "id": 3,
    "name": "Home Loan",
    "amount": 30000.0,
    "date": "2025-03-01",
    "reason": "Buying a house"
  }
  ```

---

### 4. **PUT /loans/{id}**

Update an existing loan record.

- **Request:**
  - Method: `PUT`
  - URL: `/loans/{id}`
  - Body:
  ```json
  {
    "name": "Updated Loan Name",
    "amount": 15000.0,
    "date": "2025-04-01",
    "reason": "Refinancing"
  }
  ```
  
- **Response:**
  - Status: `200 OK`
  - Body:
  ```json
  {
    "id": 1,
    "name": "Updated Loan Name",
    "amount": 15000.0,
    "date": "2025-04-01",
    "reason": "Refinancing"
  }
  ```

---

### 5. **DELETE /loans/{id}**

Delete an existing loan record.

- **Request:**
  - Method: `DELETE`
  - URL: `/loans/{id}`
    
- **Response:**
  - Status: `204 No Content`
  - Body: `None`

---

## Pagination

For GET requests that return multiple records, pagination is supported. You can use the `page` and `page_size` query parameters to retrieve specific subsets of records.

Example:
```
GET /loans?page=1&page_size=10
```

---

## Error Responses

- **400 Bad Request**: Invalid input data.
- **404 Not Found**: Resource not found.
- **500 Internal Server Error**: A server error occurred.

---

## How to Clone and Collaborate

1. **Clone the repository**  
   Use the following command to clone the repository to your local machine:
   ```bash
   git clone https://github.com/<your-username>/loan-management-api.git
   ```

2. **Install dependencies**  
   Make sure you have Python 3.x installed. Navigate to the project directory and set up a virtual environment:
   ```bash
   python -m venv .venv
   ```

   Activate the virtual environment:
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On Mac/Linux:
     ```bash
     source .venv/bin/activate
     ```

   Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the project**  
   To start the Django development server, use:
   ```bash
   python manage.py runserver
   ```

4. **Contribute to the project**  
   - Create a new branch for your changes:
     ```bash
     git checkout -b feature/your-feature-name
     ```
   - Make your changes and commit them:
     ```bash
     git add .
     git commit -m "Description of changes"
     ```
   - Push your branch:
     ```bash
     git push origin feature/your-feature-name
     ```
   - Open a pull request on GitHub to propose your changes.

---

## Conclusion

This documentation provides the basic usage of the Loan API. For more information on the API's endpoints and testing, you can refer to the Postman collection [here](https://documenter.getpostman.com/view/42403797/2sAYkHqK9z).

---
