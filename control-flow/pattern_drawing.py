

def draw_pattern():
    
    size = int(input("Enter the size of the pattern: "))
    
    
    row = 0
    
    
    while row < size:
        # Use a for loop to print asterisks side by side
        for _ in range(size):
            print("*", end="")
        
        print()
        
        row += 1


draw_pattern()
