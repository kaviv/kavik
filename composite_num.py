#include <stdio.h>
int main() 
{
  int count,num,prime= 0;
  scanf("%d", &num);
  for(count=2;count<=num/2;count++)
  {
    if((num % count) ==0)
    {
      prime =1;
      break;
    }
  }
  if(prime==0)
  {
    printf("no");
  }
  else
  {
    printf("yes");
  }
  return 0;
}
       
   
