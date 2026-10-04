from collections import Counter

from test_data import generate_user


def print_users(users_list: list):
    print("---Список сгенерированных пользаков---")
    print(*users_list, sep="\n")
    for user in users_list:
        print(f"Username: {user['username']} | Age: {user['age']} | Status: {user['status']}")

def print_statistics(users_list: list):
    status_count = Counter(user['status'] for user in users_list)
    active_count = status_count.get("ACTIVE")
    inactive_count = status_count.get("INACTIVE")
    blocked_count = status_count.get("BLOCKED")
    print("---Cтатистика по статусам---")
    print(f"Всего сгенерированных пользаков: {len(users_list)}\n"
          f"ACTIVE: {active_count}\n"
          f"INACTIVE: {inactive_count}\n"
          f"BLOCKED: {blocked_count}")


if __name__ == "__main__":
    count_users = int(input("Введите количество необходимых тестовых пользователей: "))
    generate_users = [generate_user() for _ in range(count_users)]
    print_users(generate_users)
    print_statistics(generate_users)
