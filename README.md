
# Restaurant Portfolio API Documentation

Live API Link
👉 https://restaurantprofile.onrender.com/api/


## API Overview

This backend API, built with Django REST Framework, powers the Restaurant Portfolio project. It allows managing restaurants, tags, foods, and contact inquiries.


## API Reference

####  API Endpoints

| Endpoint               | HTTP Method       | Description                                 |
|------------------------|-------------------|---------------------------------------------|
| `/api/tags/`           | GET               | List all available tags                      |
| `/api/restaurants/`    | GET, POST         | List all restaurants / Create a new one     |
| `/api/restaurants/{id}/` | GET, PUT, DELETE | Retrieve, update, or delete a restaurant by ID |
| `/api/foods/`          | GET, POST         | List all foods / Add a new food item         |
| `/api/foods/{id}/`     | GET, PUT, DELETE  | Retrieve, update, or delete a food item by ID |
| `/api/contact/`        | POST              | Submit contact inquiries                      |

#### Get item

```http
  GET /api/foods/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |




## How to Use

- Open the live API URL in your browser or use API clients like [Postman](https://www.postman.com/) or [Insomnia](https://insomnia.rest/) to test requests.
- GET requests will return JSON data lists or single items.
- POST, PUT, and DELETE requests allow creating, updating, or deleting records.
- Contact endpoint accepts POST requests for sending inquiries.
- The API uses an SQLite database in production.
- Static files are served using Whitenoise.
## Technologies Used

- Django 4.2.7
- Django REST Framework
- SQLite (production database)
- Whitenoise for static file serving
- Django CORS Headers for frontend communication

Feel free to explore the API and reach out if you'd like a frontend demo or additional documentation!

---

**Author:** Sanjana Ayshi  
**GitHub:** [https://github.com/SanjanaAyshi/restaurantProfile](https://github.com/SanjanaAyshi/restaurantProfile)


