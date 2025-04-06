import json
import unittest  # Importing unittest for writing and running test cases
from app import create_app  # Importing the Flask app factory function
from unittest.mock import MagicMock, patch  # Importing MagicMock and patch for mocking dependencies

class TestRoutes(unittest.TestCase):
    def setUp(self):
        """Set up the test client for the Flask app."""
        self.app = create_app()
        self.client = self.app.test_client()  # Creates a test client to simulate HTTP requests

    @patch('flask_mysqldb.MySQL.connection')  # Patch MySQL connection directly here
    def test_get_spartans(self, mock_connection):
        """Test the /spartans route with a mocked database connection."""

        # Mocking the cursor (a cursor in MySQL is an object used to interact with the database)
        mock_cursor = MagicMock()
        mock_connection.cursor.return_value = mock_cursor  # Mock `cursor()` to return our fake cursor

        # Mock the fetchall() method on the cursor to return the data we want
        mock_cursor.fetchall.return_value = [
            (1, 'Rick', 'Sanchez', 'rick.sanchez@citadelofricks.com', 'Multiverse Science', 'Morty Smith', '2023-01-01', '2023-12-31'),
            (2, 'Morty', 'Smith', 'morty.smith@earthdimension.com', 'Interdimensional Adventures', 'Rick Sanchez', '2023-02-01', '2023-11-30')
        ]

        # Send a GET request to /spartans
        response = self.client.get('/spartans')

        # Validate response (assertions)
        self.assertEqual(response.status_code, 200)  # Ensure request was successful
        data = json.loads(response.data)  # Parse JSON response

        # Check that the response contains the expected number of records
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['first_name'], 'Rick')  # Verify first record

