with open('input/test', 'r') as f:
    template, rules = f.read().split('\n\n')

rules_table = {}

for rule in rules.split('\n'):
    pair, insert = rule.split(' -> ')
    rules_table[pair] = insert

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def traverse(self):
        head = self.head
        while head is not None:
            print(head.data)
            head = head.next


def initialize_linked_list(template) -> Node:
    head = Node()
    cur = head
    for letter in template:
        cur.data = letter
        cur.next = Node()
        cur = cur.next
    return head


def part1(template):
    #for _ in range(2):
    head = initialize_linked_list(template)
    l = LinkedList(head)
    l.traverse()

part1(template)