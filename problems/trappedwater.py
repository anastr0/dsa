def max_water(height):
    # bruteforce 
    n = len(height)
    max_water = 0
    for i in range(n):
        
        max_left = height[i]
        for l in range(i):
            max_left = max(height[l], max_left)
        
        max_right = height[i]
        for r in range(i+1, n):
            max_right = max(height[r], max_right)
        
        max_water += (min(max_left, max_right) - height[i])
    return max_water


height = [3,0,1,0,4,0,2]
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(max_water(height))