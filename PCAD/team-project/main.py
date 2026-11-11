# Restaurant Management System

menu = {
    "Starters": [
        {
            "id": 1,
            "name": "Bread",
            "price": 4.3
        },
        {
            "id": 2,
            "name": "Item 1",
            "price": 5.9
        },
        {
            "id": 3,
            "name": "Item 2",
            "price": 3,
        }
    ],
    "Main Courses": [
        {
            'id': 4,
            "name": "Grilled Salmon",
            "price": 17
        },
        {
            "id": 5,
            "name": "Pizza",
            "price": 13.5
        },
        {  
            "id": 6,
            "name": "Steak",
            "price": 19.99
        },
        { 
            "id": 7, 
            "name": "Bruschette",
            "price": 16.99
        },
        {
            "id": 8,  
            "name": "Stuffed Mushrooms",
            "price": 22
        },
    ],
    "Desserts": [
        {
            "id": 9,
            "name": "Cheesecake",
            "price": 16
        },
        { 
            "id": 10, 
            "name": "Lemon Cake",
            "price": 14.99
        },
        {
            "id": 11,
            "name": "Vanilla Cake",
            "price": 13.5
        },
        {
            "id": 12,
            "name": "Glazzed Donut",
            "price": 7
        }
    ]
}

class Table:
    def __init__(self, table_number, capacity, status=False):
        self.table_number = table_number
        self.capacity = capacity
        self.status = status

    def occupy(self, table_number=None):
        self.status = True
        return f"Table #{self.table_number} is occupied."

    def info(self):
        return f"Table #{self.table_number}\n- Capacity: {self.capacity}\n- Is occupied: {self.status}"

class Order:
    def __init__(self, table, order_number, total=0, paid=False, items=[]):
        self.table = table
        self.total = total
        self.paid = paid
        self.items = items
        self.order_number = order_number

    def create(self,):
        self.table.occupy()
        return f"Order created for Table #{self.table}. Total: ${self.total}. Paid: {self.paid}"

    def info(self):
        items_text = "\n".join(f"- {item}" for item in self.items) 
        return f"ORDER #{self.order_number}\nTOTAL: {self.total}\nTABLE: {self.table.table_number}\nItems: \n{items_text}"


def create_order(order_number, table, items):
    total = sum(item['price'] for item in items)
    order = Order(table, order_number, total, False, [item['name'] for item in items])
    return order

def get_item_by_id(id):
    for category in menu.values():
        for item in category:
            if item["id"] == id:
                return item

def welcome():
    print("Welcome to the Restaurant Management System!")
    print("1. Create Order")
    print("2. View Order Information")
    print("3. View Table Info")
    print("4. Exit")


numbers = {
    "order_number": 0,
}

tables = [
    Table(table_number=1, capacity=4),
    Table(table_number=2, capacity=6),
    Table(table_number=3, capacity=4),
    Table(table_number=4, capacity=8),
]


def occupy_table():
    table_number = int(input("Enter table number: "))

    table = next((t for t in tables if t.table_number == table_number), None)
    if table:
        return table.occupy()
    else:
        return False


    welcome()

    choice = input("Please select an option (1-4): ")

    if choice == "4":
        print("Thank you. Goodbye!")
        break
    elif choice == "1":
        choose_item(tables[0])