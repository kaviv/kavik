s=str(input())
m=''.join([s[x:x+2][::-1] for x in rangne(0,len(s),2)])
print(m)
