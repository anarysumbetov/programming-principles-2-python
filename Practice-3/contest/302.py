def isUsual(num):
    # Handle non-positive numbers if necessary
    if num <= 0:
        return False
    
    # Repeatedly divide by the allowed prime factors
    for factor in [2, 3, 5]:
        while num % factor == 0:
            num //= factor
            
    # If the remaining number is 1, all prime factors were 2, 3, or 5
    return num == 1

# Input handling
if __name__ == "__main__":
    try:
        n = int(input())
        if isUsual(n):
            print("Yes")
        else:
            print("No")
    except ValueError:
        pass