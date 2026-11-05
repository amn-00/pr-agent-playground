def average(values):
    return sum(values) / len(values)


def report(orders):
    paid = [o["total"] for o in orders if o["paid"]]
    return f"Average paid order: {average(paid):.2f}"
