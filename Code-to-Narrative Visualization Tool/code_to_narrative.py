import ast
import networkx as nx
import matplotlib.pyplot as plt

# Example code
example_codes = [
    """
def greet(name):
    print("Hello, " + name)
    
def main():
    user_name = input("Enter your name: ")
    greet(user_name)
    
if __name__ == "__main__":
    main()
    
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
    
def main():
    num = int(input("Enter a number: "))
    result = factorial(num)
    print(f"The factorial of {num} is {result}")
    
if __name__ == "__main__":
    main()
    """,
    """
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    
def main():
    num = int(input("Enter a number: "))
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
    
if __name__ == "__main__":
    main()
    """,
       """
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    fib_series = [0, 1]
    while len(fib_series) < n:
        next_fib = fib_series[-1] + fib_series[-2]
        fib_series.append(next_fib)
    return fib_series
    
def main():
    num = int(input("Enter the number of Fibonacci terms: "))
    fib_terms = fibonacci(num)
    print("Fibonacci series:", fib_terms)
    
if __name__ == "__main__":
    main()
    
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
def main():
    nums = [5, 2, 9, 1, 5, 6]
    print("Original list:", nums)
    bubble_sort(nums)
    print("Sorted list:", nums)
    
if __name__ == "__main__":
    main()
    
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
    
def main():
    nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 13
    index = binary_search(nums, target)
    if index != -1:
        print(f"{target} found at index {index}")
    else:
        print(f"{target} not found in the list")
    
if __name__ == "__main__":
    main()
    """,
]


# Parse the code using AST
def parse_code(code):
    tree = ast.parse(code)
    functions = {}
    
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions[node.name] = {
                "name": node.name,
                "args": [arg.arg for arg in node.args.args],
                "calls": []
            }
    
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in functions:
            caller = node.func.id
            callee = node.args[0] if node.args else None
            functions[caller]["calls"].append(callee)
    
    return functions

# Generate a visualization
def visualize_narrative(functions):
    G = nx.DiGraph()
    
    for function in functions.values():
        G.add_node(function["name"], label=function["name"], shape="ellipse")
        for call in function["calls"]:
            if call:
                G.add_edge(function["name"], call.id)
    
    pos = nx.spring_layout(G, seed=42)
    node_labels = nx.get_node_attributes(G, "label")
    nx.draw_networkx_nodes(G, pos, node_size=3000, node_color='skyblue')
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=10)
    
    plt.title("Code to Narrative Visualization")
    plt.show()

def main():
    functions = parse_code(code)
    visualize_narrative(functions)

if __name__ == "__main__":
    main()
