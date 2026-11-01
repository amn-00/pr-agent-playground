def list_orders(db, sort_column):
    query = f"SELECT id, total, created_at FROM orders ORDER BY {sort_column}"
    return db.execute(query).fetchall()


def average_total(orders):
    return sum(o.total for o in orders) / len(orders)
