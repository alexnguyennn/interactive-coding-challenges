from typing import Set
from pathlib import Path
import sys

# needed to make path to linked list implementation locatable
# https://fortierq.github.io/python-import/
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))
from linked_lists.linked_list.linked_list import LinkedList, Node


class MyLinkedList(LinkedList):
    def kth_to_last_elem(self, k):
        # TODO: Implement me
        pass