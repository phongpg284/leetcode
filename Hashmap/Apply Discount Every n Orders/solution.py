class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.discount = discount
        self.n = n
        self.count = 0
        self.store = dict()
        for i in range(len(products)):
            self.store[products[i]] = prices[i]

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.count += 1
        is_discount = self.count == self.n
        total = 0
        for i in range(len(product)):
            total += self.store[product[i]] * amount[i]
        if is_discount:
            self.count = 0
            total *= ((100 - self.discount) / 100)
        return total



# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)