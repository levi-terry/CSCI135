class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0

    def print_item_cost(self):
        print("%s %d @ $%d = $%d" % (self.item_name, self.item_quantity, self.item_price,
                                    (self.item_quantity * self.item_price)))


if __name__ == "__main__":
    print("Item 1")
    first_item = ItemToPurchase()
    first_item.item_name = input("Enter the item name: ")
    first_item.item_price = int(input("Enter the item price: "))
    first_item.item_quantity = int(input("Enter the item quantity: "))
    print("Item 2")
    second_item = ItemToPurchase()
    second_item.item_name = input("Enter the item name: ")
    second_item.item_price = int(input("Enter the item price: "))
    second_item.item_quantity = int(input("Enter the item quantity: "))
    print("TOTAL COST")
    first_item.print_item_cost()
    second_item.print_item_cost()
    print("Total: $%d" % ((first_item.item_quantity * first_item.item_price) +
                          (second_item.item_quantity * second_item.item_price)))
