# tests/test_finance_app.py
import unittest
from unittest.mock import patch
from io import StringIO
from console import Console
from database import Database
from transaction import Transaction


class TestFinanceApp(unittest.TestCase):
    def setUp(self):
        self.database = Database()

    def tearDown(self):
        Database.TOTAL = 0

    @patch('builtins.input', side_effect=["Food", "-20"])
    @patch('datetime.datetime.now')
    def test_insert_transaction(self, mock_now, mock_input):
        mock_now.return_value = '2022-01-01 12:00:00'
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            Transaction.get_transaction()
            self.assertEqual(mock_stdout.getvalue().strip(
            ), "Enter the transaction description: Enter the transaction amount:")

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.database.insert_transaction()
            self.assertEqual(mock_stdout.getvalue().strip(), "")

        self.assertEqual(Database.TOTAL, -20)

    @patch('builtins.input', side_effect=["Food", "-20"])
    @patch('datetime.datetime.now')
    def test_delete_transaction(self, mock_now, mock_input):
        mock_now.return_value = '2022-01-01 12:00:00'
        self.database.insert_transaction()  # Insert a transaction for testing

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.database.delete_transaction()
            self.assertEqual(mock_stdout.getvalue().strip(), "")

        # Since the only transaction is deleted
        self.assertEqual(Database.TOTAL, 0)

    def test_initialize_total(self):
        with patch('sqlite3.connect') as mock_connect:
            with patch('sqlite3.Cursor') as mock_cursor:
                # Simulate a total from the database
                mock_cursor.fetchone.return_value = (50,)
                Database.initialize_total()
                self.assertEqual(Database.TOTAL, 50)

    # Add more tests as needed


if __name__ == '__main__':
    unittest.main()
