
---

# API Documentation

## Overview
This API provides functionality for managing loan data, including creating, retrieving, updating, and deleting loan records. The API uses Django and the Django Rest Framework to provide endpoints for loan management.

---

## Base URL
```
http://127.0.0.1:8000/api
```

---
---

## Endpoints

### 1. **GET /loans**

Retrieve all loan records.

- **Request:**
  - Method: `GET`
  - URL: `/loans`
  - Headers:
    - `Authorization: Bearer <your-jwt-token>`
    
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

Retrieve a loan record by ID.

- **Request:**
  - Method: `GET`
  - URL: `/loans/{id}`
  - Headers:
    - `Authorization: Bearer <your-jwt-token>`
    
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
  - Headers:
    - `Authorization: Bearer <your-jwt-token>`
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
  - Headers:
    - `Authorization: Bearer <your-jwt-token>`
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
  - Headers:
    - `Authorization: Bearer <your-jwt-token>`
    
- **Response:**
  - Status: `204 No Content`
  - Body: `None`

---

## Postman Collection

You can also refer to the Postman documentation for testing the API interactively:  
[View Postman Collection](https://documenter.getpostman.com/view/42403797/2sAYkHqK9z)

---

## Error Responses

- **400 Bad Request**: Invalid input data.
- **401 Unauthorized**: Missing or invalid authentication token.
- **404 Not Found**: Resource not found.
- **500 Internal Server Error**: A server error occurred.

---

## Pagination

For GET requests that return multiple records, pagination is supported. You can use the `page` and `page_size` query parameters to retrieve specific subsets of records.

Example:
```
GET /loans?page=1&page_size=10
```

---

## Conclusion

This documentation provides details on how to interact with the Loan API request methods, and expected responses. For further questions, please refer to the [Postman Collection](https://documenter.getpostman.com/view/42403797/2sAYkHqK9z).

---

