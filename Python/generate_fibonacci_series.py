# Python program to get the Fibonacci series between 0 to 50

def generate_fibonacci_series(limit):
    
    fibonacci_series = [0, 1]

    # Continue generating Fibonacci numbers until the limit is reached
    while True:
        next_number = fibonacci_series[-1] + fibonacci_series[-2]
        if next_number > limit:
            break  
        fibonacci_series.append(next_number)
        
    return fibonacci_series


limit = 50
fibonacci_series = generate_fibonacci_series(limit)

# Print the result
print(f"Fibonacci series up to {limit}: {fibonacci_series}")
  
