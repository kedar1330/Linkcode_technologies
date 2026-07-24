// Online C compiler to run C program online
#include<stdio.h>

void add_elements(int *ptr,int size){
    int sum=0;
    for (int i=0; i<size;i++){
        printf("%d\n",*(ptr+i));
        sum+=*(ptr+i);
    }
    printf("%d\n" ,sum);
}


//int *ptr=arr.:
int main() {
    int arr[5]={10,20,30,40,50};
    add_elements(arr,5);
    return 0;
}