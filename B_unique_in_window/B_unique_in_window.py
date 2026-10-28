#https://contest.yandex.ru/contest/102171/run-report/169641015/

import sys

def solve(user_ids, window_size):
    user_counts = {}
    
    for i in range(window_size):
        user_id = user_ids[i]
        user_counts[user_id] = user_counts.get(user_id, 0) + 1
    results = [len(user_counts)]

    for i in range(window_size, len(user_ids)):
        leaving_user = user_ids[i - window_size]
        entering_user = user_ids[i]
        user_counts[leaving_user] -= 1
        if user_counts[leaving_user] == 0:
            del user_counts[leaving_user]
        user_counts[entering_user] = user_counts.get(entering_user, 0) + 1
        results.append(len(user_counts))
    return results


def main():
    number_of_views, window_size = map(int, sys.stdin.readline().split())
    user_ids = list(map(int, sys.stdin.readline().split()))
    results = solve(user_ids, window_size)
    print(*results)


if __name__ == "__main__":
    main()
