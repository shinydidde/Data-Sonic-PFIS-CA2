import unittest
from flask import Flask, request
from app import app

class TestBookingForm(unittest.TestCase):
    def setUp(self):
        # Create a test client
        self.app = app.test_client()

    def test_booking_form_submission(self):
        # Simulate form submission
        form_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'check_in': '2024-04-18',
            'check_out': '2024-04-19',
            'room_type': 'Suite Room',
            'room_number': '1',
            'note': 'Test note'
        }
        response = self.app.post('/booking', data=form_data, follow_redirects=True)

        # Check if form submission was successful
        self.assertEqual(response.status_code, 200)
        # Add more assertions to check the behavior of your application after form submission

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
