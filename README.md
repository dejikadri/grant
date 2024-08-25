# Grant Application Repository

## Setup Instructions

1. **Clone the Repository**
   - Clone this repository to your local machine using Git:
     ```bash
     git clone <repository-url>
     ```
   - Navigate into the cloned repository directory:
     ```bash
     cd <repository-folder>
     ```

2. **Start the Application**
   - To start the application, run the following command:
     ```bash
     docker-compose up
     ```
   - This command will start all the necessary services in Docker containers.

## Running Tests

1. **Initialize the Docker Environment**
   - Ensure that the application is running by executing:
     ```bash
     docker-compose up
     ```

2. **Access the Backend Container**
   - Open a new terminal window.
   - Connect to the backend container by running:
     ```bash
     docker-compose exec backend bash
     ```

3. **Execute Tests**
   - Inside the Docker container's terminal, run the following command to execute all tests:
     ```bash
     python manage.py test
     ```
   - This will initiate and run all test cases within the application.

## API Endpoints Overview

1. **Create a User**
   - **Endpoint**: `[POST] /api/register`
   - Use this endpoint to create a new user account.

2. **User Login**
   - **Endpoint**: `[POST] /api/login`
   - Login with the user credentials to receive a bearer token.

3. **Apply for a Grant**
   - **Endpoint**: `[POST] /api/grants/<grant_id>/apply`
   - Use this endpoint to submit an application for a specific grant.
   - Note that the above endpoint is authenticated and requires the access token from the login endpoint
