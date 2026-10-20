def __init__(self, head):
    self.values = []
    while head:
        self.values.append(head.val)
        head = head.next
def getRandom(self):
    return random.choice(self.values)