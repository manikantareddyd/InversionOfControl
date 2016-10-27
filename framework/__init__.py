class FruitBay:
    def __init__(self,sort_machine):
        self.fruits = []
        self.sort_machine = sort_machine

    def add_fruit(self,fruit_name,fruit_price):
        self.fruits.append({'name':fruit_name,'price':fruit_price})

    def get_cheapest_fruit(self):
        sorted_fruits = self.sort_machine(self.fruits)
        return sorted_fruits[0]['name']
