#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Система управления складом

class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<{self.value}>"


def depth_limited_search(node, limit, depth=0):
    if node is None:
        return float('-inf')  # Возвращаем минимальное значение, если узел отсутствует
    if depth == limit:
        return node.value  # Возвращаем значение узла на заданной глубине

    left_value = depth_limited_search(node.left, limit, depth + 1)
    right_value = depth_limited_search(node.right, limit, depth + 1)

    # Возвращаем максимальное значение между найденными ценностями
    return max(left_value, right_value)


if __name__ == "__main__":
    root = BinaryTreeNode(
        3,
        BinaryTreeNode(1, BinaryTreeNode(0), None),
        BinaryTreeNode(5, BinaryTreeNode(4), BinaryTreeNode(6)),
    )

    limit = 2

    # Вызов функции поиска максимального значения
    max_value = depth_limited_search(root, limit)
    print(f"Максимальное значение на указанной глубине: {max_value}")