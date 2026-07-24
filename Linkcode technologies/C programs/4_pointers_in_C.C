// Pointers in C
#include <stdio.h>

int main() {
    int x=10;
    printf("%d\n" "%p\n", x, &x);
    int *ptr=&x;
    printf("%d\n" "%p\n", *ptr, ptr);
    
    //addition
    //int ans=x+2;
    int ans=*ptr+2;
    printf("%d\n", ans);
    
    int arr[3]={10,20,30};
    printf("%d\n",arr[0]);
    int *p=arr;
    printf("%d\n",*p);
    printf("%d\n",*p+2);
    printf("%d\n",*(p+2));
    
    
    for(int i=0;i<3;i++){
        printf("%d\n",*(p+i));
        
    }
    return 0;
}