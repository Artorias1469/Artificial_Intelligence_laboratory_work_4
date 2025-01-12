#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Система навигации робота-пылесоса

class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<{self.value}>"


def depth_limited_search(node, goal, limit, depth=0):
    if node is None:
        return False
    if node.value == goal:
        print(f"Найден на глубине: {depth}")
        return True
    if depth >= limit:
        return False

    # Поиск в левом и правом поддереве
    found_in_left = depth_limited_search(node.left, goal, limit, depth + 1)
    found_in_right = depth_limited_search(node.right, goal, limit, depth + 1)

    return found_in_left or found_in_right

if __name__ == "__main__":
    # Создание дерева и установка значений
    root = BinaryTreeNode(
        1,
        BinaryTreeNode(2, None, BinaryTreeNode(4)),
        BinaryTreeNode(3, BinaryTreeNode(5), None),
    )

    goal = 4
    limit = 2

    # Вызов функции поиска
    if not depth_limited_search(root, goal, limit):
        print("Не найдено")