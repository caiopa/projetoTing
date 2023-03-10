import pytest
from ting_file_management.priority_queue import PriorityQueue


small = {
    "nome_do_arquivo": "small.txt",
    "qtd_linhas": 4,
    "linhas_do_arquivo": ["alguma coisa aqui"],
}

medium = {
    "nome_do_arquivo": "medium.txt",
    "qtd_linhas": 14,
    "linhas_do_arquivo": ["alguma coisa aqui"],
}

big = {
    "nome_do_arquivo": "big.txt",
    "qtd_linhas": 40,
    "linhas_do_arquivo": ["alguma coisa aqui"],
}


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()

    priority_queue.enqueue(small)
    assert len(priority_queue) == 1

    priority_queue.enqueue(medium)
    assert len(priority_queue) == 2

    priority_queue.enqueue(big)
    assert len(priority_queue) == 3

    assert len(priority_queue) == 3
    assert len(priority_queue.high_priority) == 1
    assert len(priority_queue.regular_priority) == 2

    with pytest.raises(IndexError):
        priority_queue.search(14)

    assert priority_queue.search(1) == (medium)

    assert priority_queue.dequeue() == (small)
    assert priority_queue.dequeue() == (medium)
    assert priority_queue.dequeue() == (big)

    assert len(priority_queue) == 0
    assert len(priority_queue.high_priority) == 0
    assert len(priority_queue.regular_priority) == 0
