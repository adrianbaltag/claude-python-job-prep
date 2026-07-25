class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1


my_counter = Counter()
print(my_counter.count)
my_counter.increment()
print(my_counter.count)
