
# Flask Blog API

A simple RESTful API built with **Flask** to manage blog posts using in-memory storage. This backend-only project is perfect for learning and practicing API development without using a database.


## Features


- ✅ Create new blog posts
- ✅ Get a list of all blog posts
- ✅ Delete posts by ID
- ✅ JSON-based input/output
- ✅ Input validation and proper status codes


## Tech Stack

- **Language**: Python 3
- **Framework**: Flask
- **Database**: None (in-memory list only)
- **Tools**: Postman or cURL (for API testing

## project structure

Blog-API-project--->src/app.py----// Main Flask application
README.md # Project documentation

## Run Locally

Clone the project

```bash
  git clone https://github.com/karthickraja1106/-Blog-API-project
```

Go to the project directory

```bash
  cd backend
```

Install dependencies

```bash
  pip install flask
```

▶️ Run the App

```bash
  python app.py
```
The server will start at:

📍http://localhost:5000


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`pip install virtualenv`

`virtualenv -p python3 env`

`env/scripts/activate`



## API Reference

All endpoints are relative to this base.

---

## 🧾 Endpoints Summary

| Method | Endpoint          | Description              |
|--------|-------------------|--------------------------|
| GET    | `/posts`          | Retrieve all posts       |
| GET    | `/post/<id>`      | Retrieve particular posts       |
| POST   | `/post`          | Create a new post        |
| DELETE | `/post/<id>`| Delete a post by ID      |

---

➕ POST /posts

🔹 Description:
Creates a new blog post.

🔸 Request:
Content-Type: application/json

Body:

{
  "title": "My Blog Title",

  "content": "Blog content here...",

  "author": "Author Name"
}


🔸 Validation:
All fields are required: title, content, author.

Returns 400 Bad Request if any field is missing or JSON is invalid.

🔸 Response:
Status Code: 201 Created

Body:

{
  "id": 2,

  "title": "My Blog Title",

  "content": "Blog content here...",

  "author": "Author Name"
}

❌ DELETE /posts/<post_id>

🔹 Description:
Deletes a blog post by its ID.

🔸 Parameters:
post_id: Integer ID of the post to delete.

🔸 Example:

     DELETE /post/2

🔸 Response:

Status Code: 200 No Content – if deletion was successful.

Status Code: 404 Not Found – if post with post_id doesn’t exist     



## 🧠 Notes
The API uses in-memory storage; all data resets on server restart.

No authentication is required.

Designed for learning, testing, or internal tools.
## Demo

https://github.com/user-attachments/assets/087cabc7-949b-4f79-b394-7d0b75909319


## Authors

## 👨‍💻 Author

**Karthickraja P**  

Web Developer | Python & JavaScript Enthusiast  

📧 Email:k4rthickr001@gmail.com

🌐 GitHub: [@karthickrajap](https://github.com/karthickraja1106)  
  


