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

    def test_successful_login(self):
        # Simulate form submission with valid credentials
        form_data = {
            'email': 'test@gmail.com',
            'pass': '@Mani567'
        }
        response = self.app.post('/admin/result', data=form_data, follow_redirects=True)

        # Check if the user is redirected to the welcome page
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.location, url_for('welcome', _external=True))

        # Check if session variables are set
        with self.app as c:
            with c.session_transaction() as sess:
                self.assertTrue(sess['is_logged_in'])
                self.assertEqual(sess['email'], 'test@gmail.com')
                # Add more assertions for session variables as needed

    def test_failed_login(self):
        # Simulate form submission with invalid credentials
        form_data = {
            'email': 'test@example.com',
            'pass': 'test'
        }
        response = self.app.post('/admin/result', data=form_data, follow_redirects=True)

        # Check if the user is redirected back to the login page
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.location, url_for('login', _external=True))

        # Check if session variables are not set
        with self.app as c:
            with c.session_transaction() as sess:
                self.assertFalse(sess.get('is_logged_in', False))
                # Add more assertions for session variables as needed

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
