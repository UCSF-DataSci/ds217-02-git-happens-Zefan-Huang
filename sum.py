class MyClass:
    def __init__(self):
        self.result = []

    def sum_q (self, n, limit):
        if n == limit:
            return
        if n % 3 == 0 or n % 5 == 0:
            self.result.append(n)
        self.sum_q(n + 1, limit)


if __name__ == "__main__":
    obj = MyClass()
    obj.sum_q(0, 500)
    obj.sum_q(500, 1000)
    print(sum(obj.result))