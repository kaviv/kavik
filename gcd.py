#include<stdio.h>
int main()
{
  int N,M,GCD=0,i;
  scanf("%d %d",&N &M);
  for(i=0;i<=N && i<=M;++i)
  {
    if(N%i==0 && M%i==0)
      GCD=i;
    printf("%d",GCD);
    return 0;
    }
}
    
