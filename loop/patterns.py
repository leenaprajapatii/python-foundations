#  * * * * * * * * * *
#  * * *         * * *
#  * *             * *
#  *                 *
#  * *             * *
#  * * *         * * *
#  * * * *     * * * *
#  * * * * * * * * * * 

def print_pattern():
    for i in range(9):
        for j in range(10):
            if (j == 0 or i == 0 or i == 8 or j == 9 or 
                (j == 1 and ((1 <= i <= 3) or (5 <= i <= 7))) or 
                (j == 2 and ((1 <= i <= 2) or (6 <= i <= 7))) or 
                (j == 3 and (i == 1 or i == 7)) or 
                (j == 6 and (i == 1 or i == 7)) or 
                (j == 7 and ((1 <= i <= 2) or (6 <= i <= 7))) or 
                (j == 8 and ((1 <= i <= 3) or (5 <= i <= 7)))):
                print("*", end="")
            else:
                print(" ", end="")
        print()  # New line after each row

# Print the pattern
print_pattern()

#          *
#        * * * 
#      *   *   * 
#    *     *     *
#  * * * * * * * * *
#    *     *     *
#      *   *   *
#        * * *
#          *

for i in range(9):
    for j in range(9):
        if (j == 4 or i == 4 or i + j == 4 or i - j == 4 or j + i == 4 or j - i == 4 or j + i == 12):
            print("*", end="")
        else:
            print(" ", end="")
    print()  # New line after each row

#  *****
#     ****
#    ***
#   **
#  *
#   **
#    ***
#     ****
#      *****

def print_arrow_pattern(size=5):
    max_width = 2 * size - 1
    for i in range(max_width):
        if i < size:  # Top half (decreasing stars)
            stars = size - i
            spaces = size - 1 - i
        else:  # Bottom half (increasing stars)
            stars = i - size + 2
            spaces = i - size + 1
        
        line = " " * spaces + "*" * stars
        print(line)

# Example usage (produces your exact pattern when size=5)
print_arrow_pattern(5)

#     ***  ***  
# *      *      *
# *              *
#   *          *  
#     *      *    
#         *        

def print_dynamic_pattern(height=6, width=9):
    for i in range(height):
        for j in range(width):
            # Conditions for printing stars
            if (i == 0 and (1 <= j <= 3 or 5 <= j <= 7) or  # Top horizontal bars
                i == 1 and (j == 0 or j == 4 or j == width-1) or  # First row special points
                i == 2 and (j == 0 or j == width-1) or  # Vertical sides
                i == 3 and (j == 1 or j == width-2) or  # Diagonal in
                i == 4 and (j == 2 or j == width-3) or  # Further diagonal
                i == height-1 and j == width//2):  # Bottom center point
                print("*", end="")
            else:
                print(" ", end="")
        print()  # 

# Print the original pattern (6x9)
print_dynamic_pattern(6, 9)




#             *            
#           *  *          
#         *      *        
#     ****          ****
#   *                  *  
#     *              *    
#       *          *      
#     *              *    
#     *                *  
#     ****          ****
#         *      *        
#           *  *          
#             *            


def print_custom_pattern():
    size = 13
    for i in range(size):
        for j in range(size):
            if (i == 0 and j == 6 or
                i == 1 and (j == 5 or j == 7) or
                i == 2 and (j == 4 or j == 8) or
                i == 3 and (j <= 3 or j >= 9) or
                i == 4 and (j == 1 or j == 11) or
                i == 5 and (j == 2 or j == 10) or
                i == 6 and (j == 3 or j == 9) or
                i == 7 and (j == 2 or j == 10) or
                i == 8 and (j == 2 or j == 11) or
                i == 9 and (j <= 3 or j >= 9) or
                i == 10 and (j == 4 or j == 8) or
                i == 11 and (j == 5 or j == 7) or
                i == 12 and j == 6):
                print("*", end="")
            else:
                print(" ", end="")
        print()  # New line after each row

# Print the pattern
print_custom_pattern()

#  12345
#  67898
#  76543
#  21234
#  

k = True
s = 0
for i in range(1, 6):
    for j in range(1, 6):
        if k:
            s += 1
            if s == 9:
                k = False
        else:
            s -= 1
            if s == 1:
                k = True
        print(s, end=" ")
    print()  
    
    
#  12345
#  67892
#  34567
#  89345
#  67894

p = True
s = 0
for i in range(1, 6):
    for j in range(1, 6):
        if p:
            s += 1
            if s == 9:
                p = False
                if i == 2:  # Special condition for second row
                    s = 2
                    p = True
        else:
            s -= 1
            if s == 2:
                p = True
        print(s, end=" ")
    print()  