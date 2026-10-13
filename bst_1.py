from __future__ import annotations
from dataclasses import dataclass
import sys

sys.setrecursionlimit(2000)

@dataclass
class Node:
    key: int
    left: Node | None = None
    right: Node | None = None


def insert(root: Node | None, key: int) -> Node:
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


def search(root: Node | None, key: int) -> Node | None:
    current = root

    while current is not None:
        if key == current.key:
            return current

        if key < current.key:
            current = current.left
        else:
            current = current.right

    return None


def find_min(root: Node) -> Node:
    current = root

    while current.left is not None:
        current = current.left

    return current


def delete_node(root: Node | None, key: int) -> Node | None:
    if root is None:
        return None

    if key < root.key:
        root.left = delete_node(root.left, key)
        return root

    if key > root.key:
        root.right = delete_node(root.right, key)
        return root

    if root.left is None and root.right is None:
        return None

    if root.left is None:
        return root.right

    if root.right is None:
        return root.left

    successor = find_min(root.right)
    root.key = successor.key
    root.right = delete_node(root.right, successor.key)

    return root


def height(root: Node | None) -> int:
    if root is None:
        return 0

    left_height = height(root.left)
    right_height = height(root.right)

    return 1 + max(left_height, right_height)


def preorder(root: Node | None, result: list[int]) -> None:
    if root is None:
        return

    result.append(root.key)
    preorder(root.left, result)
    preorder(root.right, result)


def main():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
        
    parts = int(input_data[0])
    root = None
    
    for i in range(1, parts + 1):
        if i >= len(input_data):
            break
        cmd = input_data[i].split()
        if not cmd:
            continue
            
        type_cmd = cmd[0]
        
        if type_cmd == "add":
            root = insert(root, int(cmd[1]))
        elif type_cmd == "del":
            root = delete_node(root, int(cmd[1]))
        elif type_cmd == "exists":
            if search(root, int(cmd[1])) is not None:
                print("YES")
            else:
                print("NO")
        elif type_cmd == "height":
            print(height(root))
        elif type_cmd == "print":
            result = []
            preorder(root, result)
            if len(result) == 0:
                print("Empty")
            else:
                print(*result)

