# Returns all customers
customer = Customer.objects.all()

# Returns first customer in customer table
firstCustomer = Customer.objects.first()

# Return last customer in table
lastCustomer = Customer.objects.last()

# Returns single customer by name
customerByName = Customer.objects.get(name='Jane Doe')

#Returns customer by id
customerById = Customer.objects.get(id=1)

# Returns all orders related to customer (firstCustomer)
firstCustomer.order_set.all()

# Returns orders customer name
order = Order.objects.first()
parentName = order.customer.name

# Returns products with category value equal to "Outdoor"
products = Product.objects.filter(category="Outdoor")

# Return Order sort by id
leastToGreatest = Product.objects.all().order_by('id')
greatestToLeast = Product.objects.all().order_by('-id')

# Returns all products with tag of "Sports" (many-to-many relationship query)
productsFiltered = Product.objects.filter(tags__name="Sports")