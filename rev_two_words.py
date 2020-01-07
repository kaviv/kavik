#include <stdio.h>
#include <string.h>
#define MAX_SIZE 100 

int main()
{
    char str[100], rev[100];
    int len, i, index, Start,end;
    len  = strlen(str);
    index = 0;
    Start = len - 1;
    end   = len - 1;

    while(Start > 0)
    {
    
        if(str[Start] == ' ')
        {
       
            i = Start + 1;
            while(i <= end)
            {
                rev[index] = str[i];

                i++;
                index++;
            }
            rev[index++] = ' ';

            end = Start - 1;
        }

        Start--;
    }

    for(i=0; i<=end; i++)
    {
        rev[index] = str[i];
      }
    rev[index] = '\0'; 

    printf("%s", str);
    printf("%s", rev);

    return 0;
}
