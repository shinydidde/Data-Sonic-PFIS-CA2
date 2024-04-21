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
            'name': 'Mrudula',
            'email': 'mrudula@example.com',
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


class TestLogin(unittest.TestCase):
    def setUp(self):
        # Create a test client
        self.app = app.test_client()

        # Set up application context
        self.ctx = app.app_context()
        self.ctx.push()

        # Set configuration variables
        app.config['SERVER_NAME'] = 'horsevalleyresort.francecentral.cloudapp.azure.com:8080'
        app.config['APPLICATION_ROOT'] = '/'
        app.config['PREFERRED_URL_SCHEME'] = 'https'

         # Initialize session
        with self.app as c:
            with c.session_transaction() as sess:
                sess['csrf_token'] = 'test_csrf_token'

    def test_successful_login(self):
        # Simulate form submission with valid credentials
        form_data = {
            'email': 'test@gmail.com',
            'pass': '@Mani567'
        }
        response = self.app.post('/admin/result', data=form_data, follow_redirects=True)

        # Check if the response contains a redirect location
        self.assertIsNotNone(response.location)

        # If there is a redirect, check if it's the expected redirect
        if response.location:
            expected_redirect = url_for('welcome', _external=True)
            self.assertEqual(response.location, expected_redirect)

        # Check if session variables are set
        with self.app.session_transaction() as sess:
            self.assertTrue(sess['is_logged_in'])
            self.assertEqual(sess['email'], 'test@example.com')
            # Add more assertions for session variables as needed

    def test_failed_login(self):
        with self.app:
            # Simulate form submission with invalid credentials
            form_data = {
                'email': 'test@example.com',
                'pass': 'test'
            }
            response = self.app.post('/admin/result', data=form_data, follow_redirects=True)

            # Check if the response contains a redirect location
            self.assertIsNotNone(response.location)

            # If there is a redirect, check if it's the expected redirect
            if response.location:
                expected_redirect = url_for('login', _external=True)
                self.assertEqual(response.location, expected_redirect)

            # Check if session variables are not set
            with self.app.session_transaction() as sess:
                self.assertFalse(sess.get('is_logged_in', False))
                # Add more assertions for session variables as needed

    def tearDown(self):
        # Pop the application context after the test
        self.ctx.pop()

if __name__ == '__main__':
    unittest.main()
