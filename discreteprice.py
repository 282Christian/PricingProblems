from pulp import LpMaximize, LpProblem, LpVariable, lpSum, LpStatus

# Define products, price levels, and demand
products = ['Product_Standard', 'Product_Advanced', 'Product_Premium']
price_levels = {
    'Product_Standard': [4.99, 7.99, 9.99],
    'Product_Advanced': [7.99, 9.99, 12.99],
    'Product_Premium' : [12.99, 15.99, 19.99],
}
demand = {
    'Product_Standard': [200, 160, 110],
    'Product_Advanced': [160, 130, 90],
    'Product_Premium': [110, 80, 70],
}


# Create the problem
model = LpProblem(name="pricing-optimization", sense=LpMaximize)

# Define decision variables
y = {
    (j, k): LpVariable(name=f"y_{j}_{k}", cat="Binary")
    for k in products
    for j in range(len(price_levels[k]))
}

# Objective function: Maximize total revenue
model += lpSum(
    price_levels[k][j] * demand[k][j] * y[(j, k)]
    for k in products
    for j in range(len(price_levels[k]))
), "Total Revenue"

# Constraints: One price level per product
for k in products:
    model += lpSum(y[(j, k)] for j in range(len(price_levels[k]))) == 1, f"OnePriceLevel_{k}"

# Solve the problem
status = model.solve()

# Print results
print(f"Status: {LpStatus[model.status]}")  # Convert status to a descriptive string
for k in products:
    for j in range(len(price_levels[k])):
        if y[(j, k)].value() == 1:
            print(f"{k} is priced at {price_levels[k][j]} with expected demand {demand[k][j]}")
print(f"Total Revenue: {model.objective.value()}")

