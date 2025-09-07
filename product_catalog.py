from product_data import products

# Step 1 - Print out the products to see the data that you are working with.
print("Available Products:")
for product in products:
    print(product)

# Step 2 - Mock customer preferences (instead of typing input)
customer_preferences = ["eco-friendly", "durable", "compact"]  # <<< MOCK DATA
print("\nCustomer Preferences:", customer_preferences)

# Step 3 - Convert customer_preferences list to set to eliminate duplicates.
customer_tags = set(customer_preferences)

# Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []
for product in products:
    converted_products.append({
        "name": product["name"],
        "tags": set(product["tags"])
    })

# Step 5 - Function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    return len(product_tags.intersection(customer_tags))

# Step 6 - Function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''
    results = []
    for product in products:
        matches = count_matches(product["tags"], customer_tags)
        if matches > 0:  # only recommend if at least one tag matches
            results.append({"name": product["name"], "matches": matches})

    return sorted(results, key=lambda x: x["matches"], reverse=True)

# Step 7 - Call your function and print the results
recommendations = recommend_products(converted_products, customer_tags)

print("\nRecommended Products:")
for rec in recommendations:
    print(f"{rec['name']} (matches: {rec['matches']})")

# DESIGN MEMO
#
# The core logic of this program relies heavily on Python sets and loops.
# Sets are ideal for this task because they allow efficient membership tests 
# and quick mathematical operations like intersections. Specifically, the 
# count_matches function uses the intersection operation between a product’s 
# tags and the customer’s preferences to quickly identify overlapping keywords. 
# This is significantly faster than checking each tag individually with nested 
# loops, especially as the number of tags grows. The use of sets also ensures 
# that duplicates are automatically eliminated, which makes the comparisons 
# both clean and efficient.
#
# The program also depends on simple iteration. In recommend_products, we loop 
# through every product in the catalog, calculate the number of matching tags, 
# and collect results in a list. This approach guarantees that every product is 
# considered, and sorting the results by match count ensures that the most 
# relevant recommendations are presented first. The design is straightforward, 
# readable, and easy to extend in the future.
#
# If the product catalog contained 1,000 or more items, this approach would 
# still work efficiently because set operations are generally very fast (close 
# to O(1) for membership and intersection lookups). However, scalability 
# improvements could be made. For example, we could build an inverted index 
# that maps each tag directly to the products containing it. This would allow 
# us to look up only relevant products based on customer preferences, rather 
# than looping over every product in the catalog. Additionally, caching 
# frequently used results or leveraging a database with indexing could help if 
# the dataset grows into tens of thousands of products.
#
# Overall, this design balances clarity, efficiency, and scalability for a 
# medium-sized catalog while leaving room for optimization in larger systems.
