#https://contest.yandex.ru/contest/102171/run-report/169646766/

import sys


class HashTable:
    def __init__(self):
        self.capacity = 8
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]

    def _hash(self, key):
        hash_value = 0
        for char in key:
            hash_value = (hash_value * 131 + ord(char)) % 1000000007
        return hash_value % self.capacity

    def _resize(self):
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]

        for bucket in old_buckets:
            for pair in bucket:
                index = self._hash(pair[0])
                self.buckets[index].append(pair)

    def put(self, key, value):
        index = self._hash(key)
        bucket = self.buckets[index]

        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return

        bucket.append([key, value])
        self.size += 1

        if self.size / self.capacity > 0.75:
            self._resize()

    def get(self, key):
        index = self._hash(key)

        for stored_key, value in self.buckets[index]:
            if stored_key == key:
                return value

        return None

    def delete(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (stored_key, value) in enumerate(bucket):
            if stored_key == key:
                bucket.pop(i)
                self.size -= 1
                return value

        return None


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    number_of_commands = int(input_data[0])
    table = HashTable()
    results = []
    position = 1

    for _ in range(number_of_commands):
        command = input_data[position]
        position += 1

        if command == 'put':
            key = input_data[position]
            value = int(input_data[position + 1])
            position += 2
            table.put(key, value)

        elif command == 'get':
            key = input_data[position]
            position += 1

            value = table.get(key)
            if value is None:
                results.append('Error')
            else:
                results.append(str(value))

        elif command == 'del':
            key = input_data[position]
            position += 1

            value = table.delete(key)
            if value is None:
                results.append('Error')
            else:
                results.append(str(value))

        elif command == 'size':
            results.append(str(table.size))

    print('\n'.join(results))


if __name__ == '__main__':
    solve()
