Here’s a README file for the provided Flask course registration application:

---

# Course Registration Application

This is a web application built using Flask and SQLAlchemy that allows users to register for courses. Registered users' details can be viewed on a separate page, and each user entry can be deleted if needed. The application stores data in an SQLite database.

## Features

- **Course Registration Form**: Users can enter their name, email, phone number, and choose a course.
- **View Registrants**: Displays a list of registered participants, showing their name, email, course, and phone number.
- **Delete Registrant**: Option to delete individual user entries.

## Getting Started

### Prerequisites

- Python 3.x
- Flask (`pip install flask`)
- Flask-SQLAlchemy (`pip install flask_sqlalchemy`)

### Installation

1. **Clone or Download** this repository:
   ```bash
   git clone https://github.com/your-username/course-registration-app.git
   cd course-registration-app
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   python app.py
   ```
   The application will start running on `http://127.0.0.1:5000`.

### Project Structure

```
course-registration-app/
├── app.py               # Main Flask application file
└── README.md            # Project README file
```

### Usage

1. **Register**: Visit `http://127.0.0.1:5000/` to access the registration form.
2. **View Registered Participants**: Click the link to view the list of registered users.
3. **Delete Registration**: To delete a participant's entry, click the "Delete" link next to their entry on the registrations page.

### Routes

- **/**: Displays the course registration form.
- **/registrations**: Shows a list of registered participants.
- **/delete/<id>**: Deletes a specific registration.

### Code Overview

- **`app.py`**:
  - Initializes the Flask app and configures the SQLite database.
  - Defines the `Registration` model, representing the structure of the `registrations` table.
  - Contains the following routes:
    - `/`: Displays the registration form and processes form submissions.
    - `/registrations`: Displays all registered users.
    - `/delete/<id>`: Deletes a registration by ID.

- **Database Management**:
  - The `db.create_all()` command inside `app.app_context()` ensures that all tables defined in the model are created.
  - SQLAlchemy handles the addition, retrieval, and deletion of data in the database.

### Example

1. **Register**: Submit the form with details like name, email, course, and phone number.
2. **View Registrants**: Navigate to the "View Registered Participants" page to see a list of all registered users.
3. **Delete**: Click "Delete" to remove a registration from the list.

### License

This project is licensed under the MIT License.

---

> Developed by  Anjanana CV
> 

