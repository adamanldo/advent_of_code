from collections import Counter

with open("input/14", "r") as f:
    template, rules = f.read().split("\n\n")

rules_table = {}

for rule in rules.split("\n"):
    pair, insert = rule.split(" -> ")
    rules_table[pair] = insert


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def add_to_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        cur = self.head
        while cur.next:
            cur = cur.next

        cur.next = new_node

    def print_ll(self):
        out = []
        cur = self.head
        while cur is not None:
            out.append(cur.data)
            cur = cur.next
        print("".join(out))

    def get_most_common_subtract_least_common(self):
        out = []
        cur = self.head
        while cur is not None:
            out.append(cur.data)
            cur = cur.next
        llstring = "".join(out)
        c = Counter(llstring)
        print(c.most_common(1)[0][1] - c.most_common()[-1][1])

    # using the rules, find the starting index and what to insert for any potential match
    def find_rule_match_and_insert(self):
        idx_and_element_to_insert = []
        cur = self.head
        while cur is not None:
            if cur.next is None:
                break
            if cur.data + cur.next.data in rules_table:
                original_next = cur.next
                new_node = Node(rules_table[cur.data + cur.next.data])
                temp = cur.next
                cur.next = new_node
                new_node.next = temp
            cur = original_next
        return idx_and_element_to_insert


def initialize_linked_list(template) -> LinkedList:
    llist = LinkedList()
    for letter in template:
        llist.add_to_end(letter)
    return llist


def part1(template):
    llist = initialize_linked_list(template)
    for _ in range(10):
        llist.find_rule_match_and_insert()
    llist.get_most_common_subtract_least_common()


if __name__ == "__main__":
    part1(template)
