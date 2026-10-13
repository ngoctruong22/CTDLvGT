from __future__ import annotations
from dataclasses import dataclass
import sys

sys.setrecursionlimit(2000)


@dataclass
class Node:
    key: int
    left: Node | None = None
    right: Node | None = None


def insert(root, key):
    if root is None:
        return Node(key)

    current = root

    while True:
        if key == current.key:
            return root

        if key < current.key:
            if current.left is None:
                current.left = Node(key)
                return root
            current = current.left
        else:
            if current.right is None:
                current.right = Node(key)
                return root
            current = current.right

def rotate_right(root):
    x = root.left
    root.left = x.right
    x.right = root
    return x

def rotate_left(root):
    y = root.right
    root.right = y.left
    y.left = root
    return y

def left_at(root, key):
    if key < root.key:
        root.left = left_at(root.left, key)
        return root

    if key > root.key:
        root.right = left_at(root.right, key)
        return root

    return rotate_left(root)

def right_at(root, key):
    if key < root.key:
        root.left = right_at(root.left, key)
        return root

    if key > root.key:
        root.right = right_at(root.right, key)
        return root

    return rotate_right(root)

def preorder(root, result):
    if root is None:
        return

    result.append(root.key)
    preorder(root.left, result)
    preorder(root.right, result)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])

    root = None
    idx = 1
    for _ in range(n):
        root = insert(root, int(input_data[idx]))
        idx += 1

    m = int(input_data[idx])
    idx += 1

    for _ in range(m):
        command = input_data[idx]
        x = int(input_data[idx + 1])
        idx += 2

        if command == "left":
            root = left_at(root, x)
        elif command == "right":
            root = right_at(root, x)
            
        res = []
        preorder(root, res)
        print(*(res))

if __name__ == '__main__':
    main()
