n, t = map(int, input().split())

s = input()
li = list(s)
while(t>0): 
    i = 0   
    while (i< n-1):
        if(li[i]=="B" and li[i+1]=="G"):
            li[i], li[i+1] = li[i+1], li[i]
            i+=1  
        i+=1
    t-=1       

print(''.join(li))
