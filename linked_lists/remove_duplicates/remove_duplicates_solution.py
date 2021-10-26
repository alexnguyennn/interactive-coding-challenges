from typing import Set
from pathlib import Path
import sys

# needed to make path to linked list implementation locatable
# https://fortierq.github.io/python-import/
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))
from linked_lists.linked_list.linked_list import LinkedList, Node


class MyLinkedList(LinkedList):

    def remove_dupes(self):
        prev = None
        seen = set()
        if self.head == None or len(self) == 1:
            return

        cur = self.head
        self._walk_list_and_remove_dupes(cur, seen)

    #     while cur != None:
    #         if cur.data != None and prev != None and cur.data in seen:
    #             # duplicate! remove
    #             prev.next = cur.next
    #             cur = cur.next
    #             continue
            #   seen.add(current.data)
    #         prev = cur
    #         cur = cur.next

    # NOTE: not great.. hard to control pointer update for traverse for map lookup easily
    # recurse seems good for aggregate
    # def _walk_list_and_remove_dupes(self, current: Node, seen_map: Set):
    #     if current.next == None:
    #         return
    #     else:
    #         self._walk_list_and_remove_dupes(current.next, seen_map)
    #         if current.data != None and current.data in seen_map:
    #             # duplicate! remove
    #             current.next = current.next.next
    #             return
    #         seen_map.add(current.data)


