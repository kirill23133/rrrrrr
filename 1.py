n = [] 
with open('17.txt', 'r') as file: 
    for line in file.readlines():
        n.append(int(line))
 
 
cnt = 0 
mx = 0 
for i, el in enumerate(n): 
    if i <= len(n) - 2: 
        if n[i] % 5 == 0 or n[i+1] % 5 == 0: 
            sm = n[i] + n[i+1] 
            if sm % 7 == 0: 
                cnt += 1 
                if mx < sm: mx = sm 
 
print(cnt, mx)




