Contact Book Web API project:

```markdown
# Contact Book Web API

Welcome to the Contact Book Web API repository! This repository contains a FastAPI-based web API for managing a contact book. It provides endpoints to create, read, update, and delete contacts, as well as search and retrieve contacts with upcoming birthdays.

## Features

- Create, Read, Update, and Delete (CRUD) operations for contacts.
- Search contacts based on name, surname, or email.
- Retrieve contacts with birthdays in the upcoming week.

## Prerequisites

Before running the API, make sure you have the following installed:

- Python 3.x
- PostgreSQL database

## Getting Started

1. Clone this repository to your local machine.

```bash
git clone https://github.com/remmover/fastapi_verification.git
cd contact-book-web-api
```

2. Install the required Python packages using `poetry`:

```bash
poetry install
```

3. Configure the Database URL:

   Open the `src/conf/config.py` file and update the `DB_URL` with your PostgreSQL database connection URL.

4. Run the API:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

5. Open your web browser and go to `http://localhost:8000/api` to access the API documentation.

## API Endpoints

- **GET /api/contacts**: Get a list of contacts with pagination options.
- **GET /api/contacts/{contact_id}**: Get a single contact by ID.
- **POST /api/contacts**: Create a new contact.
- **PUT /api/contacts/{contact_id}**: Update an existing contact.
- **DELETE /api/contacts/{contact_id}**: Delete a contact.
- **GET /api/contacts/search/{contact_value}**: Search contacts by name, surname, or email.
- **GET /api/contacts/birthday/next-week**: Get contacts with birthdays in the upcoming week.

## Additional Instructions for Homework Integration

In this extended version of the README, we will provide guidance on how to integrate the new requirements into your existing Contact Book Web API project.

### Email Verification Mechanism

To implement the email verification mechanism for registered users, follow these steps:

1. When a user registers, generate a unique verification token associated with their account.
2. Send an email to the user containing a link with the verification token.
3. When the user clicks the link, validate the token and mark the user's email as verified in the database.

### Rate Limiting for Contact Routes

To limit the rate at which users can perform certain actions (e.g., contact creation), you can use tools like FastAPI's built-in rate limiting or external libraries such as `ratelimit`. Configure the rate limits based on your application's needs.

### Enabling CORS

To enable Cross-Origin Resource Sharing (CORS) for your REST API, you need to configure CORS middleware in your FastAPI application. This will allow your API to be accessed from different domains.

### Updating User Avatars using Cloudinary

To implement the ability for users to update their avatars using Cloudinary, you'll need to integrate Cloudinary's API into your project. Here's a general outline of the steps:

1. Sign up for a Cloudinary account and obtain API credentials.
2. Use a Cloudinary library or HTTP requests to upload and manage user avatars.
3. Implement an endpoint in your API to receive avatar uploads from users.
4. Save the Cloudinary URL or identifier for the uploaded image in your database.

### Redis-based Caching

To implement Redis-based caching, follow these steps:

1. Set up a Redis instance either locally or using a service.
2. Integrate a Redis library (e.g., `aioredis`) into your project.
3. Determine which data should be cached (e.g., user details after authorization).
4. Implement caching logic to store and retrieve data from Redis.

### Password Reset Mechanism

To implement the password reset mechanism, consider the following steps:

1. Implement an endpoint that generates a unique reset token when requested by a user.
2. Send an email to the user containing a link with the reset token.
3. When the user clicks the link, validate the token and allow them to set a new password.

## Further Instructions

Continue building upon your Contact Book Web API project by integrating the features mentioned above. Remember to keep your environment variables secure in the `.env` file and utilize Docker Compose for managing your services and databases.

Feel free to adapt and extend the existing codebase as necessary to incorporate these additional functionalities. If you encounter any challenges or have questions, don't hesitate to reach out for assistance.

Best of luck with your project, and happy coding!

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Feel free to use this merged text as your README file, and modify it further to suit your project's needs. If you have any additional questions or need more assistance, feel free to ask!
