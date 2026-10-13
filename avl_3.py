from __future__ import annotations
from dataclasses import dataclass
import sys

sys.setrecursionlimit(200000)

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

def balance(node):
    if node is None:
        return None
    update(node)
    bf = balance_factor(node)

    if bf == 2:
        if balance_factor(node.right) < 0:
            node.right = rotate_right(node.right)
        return rotate_left(node)

    if bf == -2:
        if balance_factor(node.left) > 0:
            node.left = rotate_left(node.left)
        return rotate_right(node)
        
    return node

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root
    return balance(root)

def find_min(node):
    while node.left is not None:
        node = node.left
    return node

def delete(root, key):
    if root is None:
        return None
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        
        if root.right is None:
            return root.left

        successor = find_min(root.right)
        root.key = successor.key
        root.right = delete(root.right, successor.key)
    return balance(root)

def exists(root, key):
    current = root
    while current is not None:
        if key == current.key:
            return True
        elif key < current.key:
            current = current.left
        else:
            current = current.right
    return False

def next_key(root, key):
    answer = None
    current = root
    while current is not None:
        if current.key >= key:
            answer = current.key
            current = current.left
        else:
            current = current.right
    return answer

def prev_key(root, key):
    answer = None
    current = root
    while current is not None:
        if current.key <= key:
            answer = current.key
            current = current.right
        else:
            current = current.left
    return answer

def preorder(root, result):
    if root is None:
        return
    result.append(str(root.key))
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
        command = input_data[i].split()
        if not command:
            continue
        
        operation = command[0]
        
        if operation == "add":
            x = int(command[1])
            root = insert(root, x)
        elif operation == "del":
            x = int(command[1])
            root = delete(root, x)
        elif operation == "exists":
            x = int(command[1])
            output.append("YES" if exists(root, x) else "NO")
        elif operation == "next":
            x = int(command[1])
            answer = next_key(root, x)
            output.append(str(answer) if answer is not None else "None")
        elif operation == "prev":
            x = int(command[1])
            answer = prev_key(root, x)
            output.append(str(answer) if answer is not None else "None")
        elif operation == "root":
            output.append("Empty" if root is None else str(root.key))
        elif operation == "height":
            output.append(str(height(root)))
        elif operation == "print":
            if root is None:
                output.append("Empty")
            else:
                result = []
                preorder(root, result)
                output.append(" ".join(result))
                
    sys.stdout.write("\n".join(output) + "\n")

if __name__ == "__main__":
    main()