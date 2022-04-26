# Finds the most repeating element in the array
def most_visited_user(users: list[str]) -> str:
    counter = {}
    for user_name in users:
        if user_name in counter:
            counter[user_name] += 1
        else:
            counter[user_name] = 1
    max_count = 0
    max_name = None
    for name, count in counter.items():
        if count > max_count:
            max_count = count
            max_name = name
    return max_name

