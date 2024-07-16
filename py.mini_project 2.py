class Product:
    def __init__(self, name, product_id, price, stock):
        self.name = name
        self.__product_id = product_id
        self.price = price
        self.stock = stock

    def get_product_id(self):
        return self.__product_id

    def set_product_id(self, product_id):
        self.__product_id = product_id

    def update_stock(self, quantity):
        if quantity < 0 and abs(quantity) > self.stock:
            raise ValueError("Not sufficient stock is present to remove")
        else:
            self.stock += quantity

    def __str__(self):
        return f"{self.name} {self.get_product_id()} {self.price} {self.stock}"


class Customer:
    def __init__(self, customer_id, username, email, password):
        self.__customer_id = customer_id
        self.username = username
        self.email = email
        self.__password = password
    
    def get_customer_id(self):
        return self.__customer_id

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    def __str__(self):
        return f"{self.get_customer_id()} {self.username} {self.email} {self.get_password()}"


from datetime import datetime

class Order:
    def __init__(self, order_id, customer, products):
        self.__order_id = order_id
        self.customer = customer
        self.products = products
        self.order_date = datetime.now()
        self.total = sum(product.price for product in products)

    def get_order_id(self):
        return self.__order_id

    def set_order_id(self, order_id):
        self.__order_id = order_id

    def __str__(self):
        product_str = ", ".join([product.name for product in self.products])
        return f"Order {self.get_order_id()} by {self.customer.username} on {self.order_date} - Total: ${self.total}. Products: {product_str}"


class ProductService:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.get_product_id() in self.products:
            raise ValueError("Product ID already exists")
        self.products[product.get_product_id()] = product

    def get_product(self, product_id):
        return self.products.get(product_id, None)

    def update_stock(self, product_id, quantity):
        if product_id in self.products:
            self.products[product_id].update_stock(quantity)
        else:
            raise ValueError("Product not found")


class CustomerService:
    def __init__(self):
        self.customers = {}

    def add_customer(self, customer):
        if customer.get_customer_id() in self.customers:
            raise ValueError("Customer ID already exists")
        self.customers[customer.get_customer_id()] = customer

    def get_customer(self, customer_id):
        return self.customers.get(customer_id, None)


class OrderService:
    def __init__(self):
        self.orders = {}

    def place_order(self, order):
        if order.get_order_id() in self.orders:
            raise ValueError("Order ID already exists")
        self.orders[order.get_order_id()] = order

    def get_order(self, order_id):
        return self.orders.get(order_id, None)


class Delivery:
    def __init__(self, delivery_id, order, address, delivery_date=None):
        self.__delivery_id = delivery_id
        self.order = order
        self.address = address
        self.delivery_date = delivery_date if delivery_date else datetime.now()
        self.status = "Pending"

    def get_delivery_id(self):
        return self.__delivery_id

    def set_delivery_id(self, delivery_id):
        self.__delivery_id = delivery_id

    def update_status(self, status):
        self.status = status

    def __str__(self):
        return f"Delivery {self.get_delivery_id()} for Order {self.order.get_order_id()} on {self.delivery_date} at {self.address} - Status: {self.status}"


class DeliveryService:
    def __init__(self):
        self.deliveries = {}

    def add_delivery(self, delivery):
        if delivery.get_delivery_id() in self.deliveries:
            raise ValueError("Delivery ID already exists")
        self.deliveries[delivery.get_delivery_id()] = delivery

    def get_delivery(self, delivery_id):
        return self.deliveries.get(delivery_id, None)

    def update_status(self, delivery_id, status):
        if delivery_id in self.deliveries:
            self.deliveries[delivery_id].update_status(status)
        else:
            raise ValueError("Delivery not found")


# Initialize services
product_service = ProductService()
customer_service = CustomerService()
order_service = OrderService()
delivery_service = DeliveryService()

# Create and add a customer
customer = Customer("a101", "abc", "abc@gmail.com", "abc123")
customer_service.add_customer(customer)

# Create and add a product
product1 = Product("Android", "p101", 50000, 10)
product_service.add_product(product1)

# Create and place an order
order = Order("o101", customer, [product1])
order_service.place_order(order)

# Print customer, product, and order details
print(customer_service.get_customer("a101"))
print(product_service.get_product("p101"))
print(order_service.get_order("o101"))

# Create and add a delivery
delivery = Delivery("d101", order, "Kolkata")
delivery_service.add_delivery(delivery)

# Print delivery details
print(delivery_service.get_delivery("d101"))

# Update delivery status and print again
delivery_service.update_status("d101", "Delivered")
print(delivery_service.get_delivery("d101"))
