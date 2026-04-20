def canjump(num):
    max_reach = 0
    for i in range(len(num)):
        if i > max_reach:
            return False
        
        max_reach = max(max_reach, i + num[i])

        if max_reach >= len(num) - 1:
            return True
    
    return True 

num = [2, 3, 4, 1, 1, 4]
print(canjump(num))