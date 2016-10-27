Inversion of Control
---

# Introduction

This sample implements IoC and compares the approach with a traditional formulation of the same problem.

Inversion of Control (IoC) increases the modularity of program and introduce flexibilty to add run time components and perform independent testing of individual components without worrying about the dependencies. 

We'll view IoC as Dependency Injection (DI). We'll essentially decouple the dependencies between layers through some shared abstractions. 

This sample is written in python 2.7 and depends on pip2 package simplejson.

The directory structure will be explained later.

# Use - Case

The user in the end has the capability to create instances of a class called **FruitBay**. 

FruitBay is capable of storing fruit names and their corresponding prices.

It can also provide with the cheapest fruit.

# Implementation

FruitBay provides two methods.
+ FruitBay.add_fruit
    + usage: `FruitBay.add_fruit(fruit_name="Apple",fruit_price="20")`
    + returns: None
+ FruitBay.get_cheapest_fruit
    + usage: `FruitBay.get_cheapest_fruit()`
    + returns: Name of the cheapest fruit, added till now

## Traditional
Here is the traditional implementation of FruitBay

```
class FruitBayTraditional:
    def __init__(self):
        self.fruits = []

    def add_fruit(self,fruit_name,fruit_price):
        self.fruits.append({'name':fruit_name,'price':fruit_price})

    def get_cheapest_fruit(self):
        sorted_fruits = sorted(self.fruits, key=lambda k: k['price'])
        return sorted_fruits[0]['name']

fuku = FruitBayTraditional()
fuku.add_fruit("Apple",12)
fuku.add_fruit("PineApple",1)
fuku.add_fruit("Grape",34)

print fuku.get_cheapest_fruit()
```

---

## Inducing Dependency

In the `get_cheapest_fruit` we could have used any sorting algorithm. So it would be better if we fragment the code as follows.

```
class FruitBayFragmented:
    def __init__(self,sort_machine):
        self.fruits = []
        self.sort_machine = sort_machine

    def add_fruit(self,fruit_name,fruit_price):
        self.fruits.append({'name':fruit_name,'price':fruit_price})

    def get_cheapest_fruit(self):
        sorted_fruits = self.sort_machine(self.fruits)
        return sorted_fruits[0]['name']

def my_sort_machine(x):
    return sorted(x, key=lambda k: k['price'])

fuku = FruitBayFragmented(my_sort_machine)
fuku.add_fruit("Apple",12)
fuku.add_fruit("PineApple",1)
fuku.add_fruit("Grape",34)

print fuku.get_cheapest_fruit()
```

So we could have had any generic algorithm in the `my_sort_machine` method. Notice that `FruitBayFragmented` has no idea about the implementation of `sort_machine` within its implementation, except that it takes an input of a dictionary and produces a dictionary as an output.

Now we could have allowed the client to choose the method. To push it further we could have asked the client to implement their own sort.
