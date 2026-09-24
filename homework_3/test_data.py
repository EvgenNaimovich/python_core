import random
import string


def generate_login(length=8):
    return "user_" + "".join(random.choices(string.ascii_letters + string.digits, k=length))


def generate_age(min_age=18, max_age=70):
    return random.randint(min_age, max_age)


def generate_status():
    statuses = ["ACTIVE", "BLOCKED", "INACTIVE"]
    return random.choice(statuses)


def generate_user():
    return {
        "username": generate_login(),
        "age": generate_age(),
        "status": generate_status()
    }