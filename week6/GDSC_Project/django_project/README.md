

---

# Blog API (Rest API CRUD with Django Rest Framework)

A **Django-based Blog API** with **CRUD (Create, Read, Update, Delete)** functionality. This API is built using the **Django Rest Framework (DRF)** and serves blog data in JSON format. It supports pagination for fetching posts and allows authentication (if implemented).

## Features
- **CRUD Operations**: Create, Read, Update, Delete blog posts.
- **Pagination**: Results are paginated, allowing efficient data fetching.
- **Post Details**: View the title, content, and date of the posts.
- **DRF Integration**: Full integration with Django Rest Framework for building REST APIs.

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/your-repository.git
cd your-repository
```

### 2. Set Up a Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Database
Make sure you have PostgreSQL or SQLite set up. For SQLite (default in this project):

```bash
python manage.py migrate
```

### 5. Start the Server
```bash
python manage.py runserver
```

### 6. Access the API
The API will be accessible at:

```
http://127.0.0.1:8000/posts/
```

## API Endpoints

### 1. `GET /posts/`
- **Description**: Fetch a list of all blog posts with pagination.
- **Response**:

```json
{
  "count": 9,
  "next": "http://127.0.0.1:8000/posts/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "Blog 2",
      "content": "Second Post Content",
      "date_posted": "2018-08-28T02:55:29.858405Z"
    },
    {
      "id": 2,
      "title": "Blog 3",
      "content": "Third Post Content!",
      "date_posted": "2018-08-28T03:05:27Z"
    },
    ...
  ]
}
```

### 2. `GET /posts/{id}/`
- **Description**: Fetch a single post by its `id`.
- **Response**:

```json
{
  "id": 1,
  "title": "Blog 2",
  "content": "Second Post Content",
  "date_posted": "2018-08-28T02:55:29.858405Z"
}
```

### 3. `POST /posts/`
- **Description**: Create a new blog post.
- **Request Body**:
```json
{
  "title": "My New Blog Post",
  "content": "This is the content of my new blog post."
}
```
- **Response**: The newly created post, including its `id`.

### 4. `PUT /posts/{id}/`
- **Description**: Update an existing blog post.
- **Request Body**:
```json
{
  "title": "Updated Blog Post Title",
  "content": "Updated content for the blog post."
}
```
- **Response**: The updated post.

### 5. `DELETE /posts/{id}/`
- **Description**: Delete a blog post.
- **Response**: A success message, or an error if the post doesn't exist.

## Testing with Postman

You can import the Postman collection to test the API. Follow these steps:

1. Download the Postman collection: [Download Postman Collection](https://documenter.getpostman.com/view/42403797/2sB2cPk5ic).
2. Import the collection into Postman.
3. Test the different endpoints by sending requests to the API.

## Running Tests

To run the tests for your project, use:

```bash
python manage.py test
```

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and create a pull request.

## License

This project is open-source and available under the [MIT License](LICENSE).


---
