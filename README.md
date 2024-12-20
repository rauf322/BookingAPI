# BookingAPI


This is API designed to manage a booking system for hotels. It supports user authentication, hotel information retrieval, room management, and booking operations. Below is a detailed description of the features and endpoints provided by the API.

## Features

### 1. **Authentication**
- **Register**: Create a new user account.
- **Login**: Authenticate users with their credentials.
- **Logout**: End the current session for a user.
- **Auth Me**: Retrieve user details, including email and password.

### 2. **Hotels**
- Retrieve a list of all available hotels with detailed information.

### 3. **Rooms**
- View information about hotel rooms, including:
  - The associated hotel (using a foreign key).
  - Quantity of available rooms.
  - Price per room.

### 4. **Bookings**
- **Create a Booking**: Reserve rooms in a specific hotel.
- **View Bookings**: Check details of all your bookings.
- **Delete a Booking**: Cancel an existing reservation.

---

## Endpoints

### **Authentication**
| Method | Endpoint       | Description                   |
|--------|----------------|-------------------------------|
| POST   | `/auth/register` | Register a new user.          |
| POST   | `/auth/login`    | Log in an existing user.       |
| POST   | `/auth/logout`   | Log out the current user.      |
| GET    | `/auth/me`       | Retrieve current user details. |

![img.png](app/static/images/img.png)

### **Hotels**
| Method | Endpoint             | Description                  |
|--------|----------------------|------------------------------|
| GET    | `/hotels/all_hotels` | Get information about hotels.|

![img.png](app/static/images/img_1.png)

### **Rooms**
| Method | Endpoint            | Description                                                   |
|--------|---------------------|---------------------------------------------------------------|
| GET    | `/rooms/view_rooms` | Get info of particular room or information about all of them. |
     |

![img.png](app/static/images/img1.png)

### **Bookings**
| Method | Endpoint                   | Description                          |
|--------|----------------------------|--------------------------------------|
| POST   | `/bookings/rooms_amount`   | Create a new booking.                |
| GET    | `/bookings/my_booking`     | Retrieve a list of user bookings.    |
| DELETE | `/bookings/delete_booking` | Delete a specific booking.           |

![img.png](app/static/images/img_2.png)
---


## Environment Setup

To properly configure the application, you need to create a `.env` file in the root directory of your project. This file will store sensitive configuration values such as database credentials and JWT secrets.

### Steps:

1. **Create the `.env` file**:
   
   In the root directory of your project, create a file named `.env`.

2. **Add the required environment variables**:
   
   Add the following variables to the `.env` file:

   ```env
   DB_HOST=your_database_host
   DB_PORT=your_database_port
   DB_USER=your_database_user
   DB_PASS=your_database_password
   DB_NAME=your_database_name
   JWT_KEY=your_jwt_secret_key
   ALGORITHM=your_algorithm
    ```
