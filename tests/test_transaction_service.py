import unittest
from decimal import Decimal
from services.transaction_service import add_transaction
from data.models import Transaction
from unittest.mock import patch

class Transaction_Should(unittest.TestCase):

    @patch("services.transaction_service.insert_query")
    def test_AddTransaction_returns_id_when_data_is_correct(self, mock_insert):
        mock_insert.return_value = 5
        a_transaction = Transaction(amount=Decimal("10.50"), description='test', type='expense', category_id=2)

        result = add_transaction(a_transaction)

        self.assertEqual(5, result)
        mock_insert.assert_called_once()