from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def get_price(self):
        pass

    def display_details(self):
        print("Product Name:", self.name)
        print("Price:", self.get_price())


class Electronics(Product):
    def __init__(self, name, price, brand, warranty):
        super().__init__(name, price)
        self.brand = brand
        self.warranty = warranty

    def get_price(self):
        return self.price

    def display_details(self):
        super().display_details()
        print("Brand:", self.brand)
        print("Warranty:", self.warranty)

class Clothing(Product):
    def __init__(self, name, price, size, color, material):
        super().__init__(name, price)
        self.size = size
        self.color = color
        self.material = material

    def get_price(self):
        return self.price

    def display_details(self):
        super().display_details()
        print("Size:", self.size)
        print("Color:", self.color)
        print("Material:", self.material)


class Books(Product):
    def __init__(self, name, price, author, genre):
        super().__init__(name, price)
        self.author = author
        self.genre = genre

    def get_price(self):
        return self.price

    def display_details(self):
        super().display_details()
        print("Author:", self.author)
        print("Genre:", self.genre)


# Example usage
if __name__ == "__main__":
    electronics_product = Electronics("Laptop", 1000, "Dell", "1 year")
    clothing_product = Clothing("T-Shirt", 25, "M", "Red", "Cotton")
    book_product = Books("Python Programming", 50, "John Doe", "Programming")

    print("Electronic Product:")
    electronics_product.display_details()

    print("\nClothing Product:")
    clothing_product.display_details()

    print("\nBook Product:")
    book_product.display_details()























