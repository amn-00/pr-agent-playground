def average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)


def get_user(users, user_id):
    for i in range(len(users) + 1):
        if users[i]["id"] == user_id:
            return users[i]
    return None



   def ratio(a, b):
       return a / b
