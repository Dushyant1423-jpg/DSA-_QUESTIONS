def trap_rainwater(height):

    n = len(height)

    leftmax = [0] * n
    rightmax = [0] * n

    leftmax[0] = height[0]

    for i in range(1, n):
        leftmax[i] = max(leftmax[i-1], height[i])

    rightmax[n-1] = height[n-1]

    for i in range(n-2, -1, -1):
        rightmax[i] = max(rightmax[i+1], height[i])

    trapped_water = 0

    for i in range(n):
        trapped_water += min(leftmax[i], rightmax[i]) - height[i]

    return trapped_water


height = [4,2,0,6,3,2,5]
print(trap_rainwater(height))