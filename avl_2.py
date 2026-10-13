from __future__ import annotations
from dataclasses import dataclass
import sys

sys.setrecursionlimit(2000)

@dataclass
class Node:
    key: int
    left: "Node | None" = None
    right: "Node | None" = None
    height: int = 1


def height(node):
    if node is None:
        return 0
    return node.height


def update(node):
    node.height = 1 + max(height(node.left), height(node.right))


def balance_factor(node):
    return height(node.right) - height(node.left)


def rotate_right(node):
    child = node.left
    node.left = child.right
    child.right = node

    update(node)
    update(child)

    return child


def rotate_left(node):
    child = node.right
    node.right = child.left
    child.left = node

    update(node)
    update(child)

    return child


def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root

    update(root)

    balance = balance_factor(root)

    if balance == 2:
        if balance_factor(root.right) >= 0:
            return rotate_left(root)
        else:
            root.right = rotate_right(root.right)
            return rotate_left(root)

    if balance == -2:
        if balance_factor(root.left) <= 0:
            return rotate_right(root)
        else:
            root.left = rotate_left(root.left)
            return rotate_right(root)

    return root


def exists(root, key):
    current = root

    while current is not None:
        if current.key == key:
            return True
        elif key < current.key:
            current = current.left
        else:
            current = current.right

    return False


def preorder(root, result):
    if root is None:
        return

    result.append(root.key)
    preorder(root.left, result)
    preorder(root.right, result)


def main():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    q = int(input_data[0])
    
    root = None
    output = []
    
    for i in range(1, q + 1):
        line = input_data[i].strip()
        if not line:
            continue
            
        parts = line.split()
        command = parts[0]
        
        if command == "add":
            x = int(parts[1])
            root = insert(root, x)
            
        elif command == "exists":
            x = int(parts[1])
            if exists(root, x):
                output.append("YES")
            else:
                output.append("NO")
                
        elif command == "root":
            if root is None:
                output.append("Empty")
            else:
                output.append(str(root.key))
                
        elif command == "height":
            output.append(str(height(root)))
            
        elif command == "print":
            if root is None:
                output.append("Empty")
            else:
                result = []
                preorder(root, result)
                output.append(" ".join(map(str, result)))

    print("\n".join(output))

if __name__ == "__main__":
    main()