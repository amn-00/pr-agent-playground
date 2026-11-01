from app.orders import average_total, list_orders

# Only these columns can be sorted on; anything else falls back to newest first.
SORT_COLUMNS = {"newest": "created_at DESC", "total": "total DESC"}


def orders_page(db, request):
    column = SORT_COLUMNS.get(request.args.get("sort"), "created_at DESC")
    orders = list_orders(db, column)
    return {"orders": orders, "average": average_total(orders)}
