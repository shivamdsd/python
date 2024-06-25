items = ['apple', 'banans', 'cherry', 'apricot', 'text', 'coconut', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'papaya', 'quince', 'raspberry', 'strawberry', 'tangerine', 'watermelon', 'zucchini']

# First step is understanding the problem


# second step is to formulate an algorithm
# 1. Iterate through all the items in the list 
# 2. Check if the item starts with the letter 'a'
# 3. Then we have to check is there is key with the first letter of the item in the dictionary
# 4. if the key exists, then we have to append the item to the list of values of the key
# 5. if the key does not exist, then we have to create a new key with the first letter of the item and assign the item to the key


# Third step is dry run the algorithm with an example

# Fourth step is to implement the algorithm means write the code
a = 2
def group_items(items):
    result = {}
    for item in items:
        key = item[0]
        if key not in result:
            result[key] = []
        result[key].append(item)
    return result

print(group_items(items))
