#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Поиск с ограничением глубины

# Псевдокоды для необходимых классов и функций для демонстрации
class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent

    def __len__(self):
        return self.depth()  # Метод, возвращающий глубину узла

    def depth(self):
        # Возвращает глубину узла
        d = 0
        current = self
        while current.parent is not None:
            d += 1
            current = current.parent
        return d


class LIFOQueue:
    def __init__(self, items=None):
        if items is None:
            items = []
        self.items = items

    def pop(self):
        return self.items.pop() if self.items else None

    def append(self, item):
        self.items.append(item)

    def __bool__(self):
        return bool(self.items)


FAILURE = "FAILURE"
CUTOFF = "CUTOFF"


def is_cycle(node):
    # Проверка на цикл (заглушка)
    return False


def expand(problem, node):
    # Возвращает список дочерних узлов (заглушка)
    return [Node("child_state", node)]  # Здесь должно быть логика создания дочерних узлов


def depth_limited_search(problem, limit=10):
    """Ищет самые глубокие узлы в дереве поиска.

    :param problem: A Problem instance
    :param limit: Максимальная глубина поиска
    :return: Node instance or const CUTOFF or FAILURE
    """

    frontier = LIFOQueue([Node(problem.initial)])
    result = FAILURE
    while frontier:
        node = frontier.pop()
        if problem.is_goal(node.state):
            return node
        elif len(node) >= limit:
            result = CUTOFF
        elif not is_cycle(node):
            for child in expand(problem, node):
                frontier.append(child)
    return result