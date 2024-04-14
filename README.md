# Horse Valley Resort Management System

## Requirements:
### Users:

#### Admin: Manages resort information, bookings, staff, etc.
#### Staff: Handles bookings, guest requests, etc.
#### Guests: Make reservations, view amenities, etc.
### Data Requirements:

#### Resort information: Name, location, contact details, amenities, etc.
#### Guest information: Name, contact details, reservation details, etc.
#### Staff information: Name, contact details, role, schedule, etc.
#### Booking information: Guest details, check-in/out dates, room type, etc.

### Functionality:

#### Search: Guests should be able to search for available rooms based on dates and preferences.
#### Sorting: Results should be sortable by price, room type, etc.
#### Entry: Staff should be able to add/update guest and booking information.
#### Update: Admin should be able to update resort information, staff details, etc.
#### Validation: Ensure that entered data is valid and follows certain rules (e.g., valid email format, available room for booking).
#### Integrity: Maintain data integrity by proper database design and constraints.
#### Reporting: Generate reports on bookings, revenue, occupancy rates, etc.


## System Architecture:

### Backend:

Python Flask framework for the backend server.
MySQL database to store resort, guest, staff, and booking information.
Firebase for authentication

### Frontend:

HTML and CSS for the user interface.
JavaScript for client-side interactivity.
API endpoints to interact with the backend.

## Implementation Steps:
1. Set up MySQL database tables for the required entities.
2. Implement Python Flask backend to handle API requests and interact with the database.
3. Create HTML/CSS templates for the frontend.
4. Implement JavaScript for client-side functionality.
5. Test the system thoroughly, including data entry, search, validation, etc.
6. Document the implementation, including database schema, API endpoints, frontend structure, and usage instructions.


## Steps to run the project

Clone the git repo

```bash
cd Data-Sonic-PFIS-CA2
python3 app.py
```


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[Horse Valley Resort](https://horsevalleyresort.francecentral.cloudapp.azure.com:8080)
