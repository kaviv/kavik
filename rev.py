n=int(input())
rev=0
if n>0 :
	dig=n%10
    rev=rev*10+dig
    n=n/10
    print(rev)
