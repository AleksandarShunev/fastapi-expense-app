from data.models import Transaction
from data.database import insert_query


def add_transaction(transaction: Transaction):
    added_transaction = insert_query('''
    INSERT INTO transactions (amount, description, entry_date, type, category_id)
    VALUES (?,?,?,?,?)
    ''', (transaction.amount, transaction.description, transaction.entry_date,
           transaction.type, transaction.category_id))
    
    return added_transaction