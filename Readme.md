Inversion of Control
---

# Introduction

This sample implements IoC and compares the approach with a traditional formulation of the same problem.

Inversion of Control (IoC) increases the modularity of program and introduce flexibilty to add run time components and perform independent testing of individual components without worrying about the dependencies. 

We'll view IoC as Dependency Injection (DI). We'll essentially decouple the dependencies between layers through some shared abstractions. 

This sample is written in python 2.7 and depends on pip2 package simplejson.

# Use - Case

The user in the end has the capability to create instances of a class called **FruitBay**. 

FruitBay provides two methods.
+ FruitBay.add_fruit
    > usage: FruitBay.add_fruit(fruit_name="Apple",fruit_price="20")
    > returns: None
+ FruitBay.get_cheapest_fruit
    > usage: FruitBay.get_cheapest_fruit()
    > returns: Name of the cheapest fruit, added till now

Here is the traditional implementation of FruitBay

<raw>

class FruitBayTraditional:
    def __init__(self):
        self.fruits = []

    def add_fruit(self,fruit_name,fruit_price):
        self.fruits.append({'name':fruit_name,'price':fruit_price})

    def get_cheapest_fruit(self):
        sorted_fruits = sorted(self.fruits, key=lambda k: k['price'])
        return sorted_fruits[0]['name']

</raw>