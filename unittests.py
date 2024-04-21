import unittest
from flask import url_for
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

class TestAvailabilityForm(unittest.TestCase):
    def setUp(self):
        # Create a test client
        self.app = app.test_client()

    def test_availability_form_submission(self):
        # Simulate form submission
        form_data = {
            'startDate': '2024-04-18',
            'endDate': '2024-04-19',
        }
        response = self.app.post('/', data=form_data, follow_redirects=True)

        # Check if form submission was successful
        self.assertEqual(response.status_code, 200)
        # Add more assertions to check the behavior of your application after form submission

    def tearDown(self):
        pass


class TestButtonRedirect(unittest.TestCase):
    def setUp(self):
        # Create a test client
        self.app = app.test_client()

    def test_button_click_and_redirect(self):
        # Simulate clicking the button
        response = self.app.post('/room/1', data={}, follow_redirects=True)

        # Check if the response status code is a redirect (e.g., 302)
        self.assertEqual(response.status_code, 302)

        # Check if the redirected URL matches the expected URL
        expected_redirect_url = url_for('/booking/1', id='1')
        self.assertEqual(response.location, expected_redirect_url)

    def tearDown(self):
        pass



if __name__ == '__main__':
    unittest.main()
