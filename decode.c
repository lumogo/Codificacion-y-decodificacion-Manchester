#include "stdio.h"
#include "stdlib.h"
#include "math.h"
int main()
{
    int Data[] = {1,0,0,1};  //Data array
         
    int decode[] = {0,0}; 
 
/******************************************************************************
    Initialis/Print Data array
******************************************************************************/
 
 
    int a=0;
 
 
    printf("\nBinary Sample is:\n");
 
 
    for(a=0; a<4; a++)
    {
         
        printf("%d", Data[a]);
    }    
    printf("\n");
 
 
/*******************************************************************************
    Initialise/Print Decode array
*******************************************************************************/
     
    int b=0;
 
 
    printf("\nDecoded data array set to 0:\n");
 
 
    for(b=0; b<2; b++)
    {
        printf("%d", decode[b]);
    }    
    printf("\n\n");
 
 
 
 
/*******************************************************************************
    Test for bit patterns
*******************************************************************************/
 
 
    int c;
    int d;
    a=0;    
    b=0;
 
 
    printf("Testing bit pattern.....\n");
 
 
    for(c=0;c<4;c++)
    {
        printf("\nProcessing instance bits %d & %d... \n",c++,c);        
        printf("\nData will be put into decode @ %d \n",b);
 
 
        if(Data[c] == 1 && Data[c++] == 0)
        {
        printf("\ntest 1 PASS\n");
        decode[b] = 0 ;
        printf("\nData bits %d & %d converted\n", c++,c);
        printf("\nConverted bit is %d \n",decode[b]);
        printf("\nNext TEST\n");    
        b+1;
 
 
        }
        else if(Data[c] == 0 && Data[c++] == 1)
        {
 
 
        printf("stage 2 PASS\n");
        decode[b] = 1;
        printf("\nData bits %d & %d converted\n", c,c++);
        printf("\nConverted bit is %d \n",decode[b]);
        b+1;
        printf("\nNext TEST\n");
        }
        else (printf("Error"));
         
    }
 
 
    printf("\nDecoded data is %d",decode[b]);
     
    for(b=0; b<2; b++)
    {
         
        printf("%d", decode[b]);
    }    
    printf("\n\n");
 
 
    return 0;
}