import typing


# base node class
# has key, value and pointers to prev and next
class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    # init LRU cache with a capcity
    def __init__(self, capacity: int):
        self.capacity = capacity
        # node_map is to help with accessing the nodes in O(1) time
        self.node_map: typing.Dict[int, Node] = {}
        # dummy head and tail nodes
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        # set head.next to tail and tail.prev to head
        self.head.next = self.tail
        self.tail.prev = self.head

    # add node to head
    def insert_to_head(self, node: Node) -> None:
        head_next = self.head.next  # should be self.tail
        head_next.prev = node  # tail.prev = node
        node.next = head_next  # node.next = tail
        node.prev = self.head
        self.head.next = node

    # remove node from ll
    def remove(self, node: Node) -> None:
        # set previous node next to the node after the node being passed in
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key in self.node_map:
            # we want to remove the node then re-add it into the cache
            # because it counts as a "use"
            self.remove(self.node_map[key])
            # re-add the node to the doubly LL
            self.insert_to_head(self.node_map[key])
            # return the value of the node we just accessed
            return self.node_map[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # if the key is in the node_map, we just want to remove and insert and then update the value
        if key in self.node_map:
            self.remove(self.node_map[key])
            self.insert_to_head(self.node_map[key])
            self.node_map[key].val = value
        else:
            # if the node doesnt exist, we want to create it and insert it to the head
            node = Node(key, value)
            self.insert_to_head(node)
            # finally add it to the node_map
            self.node_map[key] = node

        # if the node_map contains too many keys, we want to remove the "tail" node
        # not the actual tail node as thats a dummy node
        if len(self.node_map) > self.capacity:
            node_to_remove = self.tail.prev
            self.remove(node_to_remove)
            self.node_map.pop(node_to_remove.key)
            # and remove it from the node_map

        # print(self.node_map)
        # print(self.head.next)
        # print(self.tail.prev)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
