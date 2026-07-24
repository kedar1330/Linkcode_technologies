// Online C compiler to run C program online
#include <stdio.h>
//with return type without arguement
 int sqr(){
     return 10*10;
 };
 //with return type with arguement
 //2nos-->add--->cube--->call
 int function1(int a, int b){
    int c=a+b;
    int cube=c*c*c;
    return cube;
 }
 
 
//without return type without arguement
void welcome(){
    printf("Hello! Welcome to linkcode");
}
//without return type with arguement
void welcome(char name[100]){
    printf("Hello %s ! welcome to linkcode", name);
    
}
int main() {
    //funtion call
    int op=sqr();
    printf("%d\n",op);//method 1 function call
    printf("%d\n",sqr());//method 2 function call
    
    //for next function function1 call and multiply by 2
    int f_op=function1(2,3);
    printf("%d\n",f_op*2);
    //function call for welcome
    welcome();
    //function call with arguement
    char name[100];
    printf("enter your name!\n");
    scanf("%s",name);
     welcome();
    return 0;
}

//-------------------------------------------------------------------------------------


// Online C compiler to run C program online
#include <stdio.h>
//without return type with arguement
void welcome(char name[100]){
    printf("Hello %s ! welcome to linkcode", name);
    
}
int main() {
    // Write C code here
    //function call with arguement
    char name[100];
    printf("enter your name!\n");
    scanf("%s",name);
       welcome(name);

    return 0;
}
//-----------------------------------------------------------------------
//Structure in C
// Online C compiler to run C program online
#include <stdio.h>
#include<string.h>
//structure in C
struct student{
    int rollno;
    char name[100];
    int age;
    float marks;
    
};
int main() {
    struct student s;
    //assign
    s.rollno=101;
    strcpy(s.name,"ram");
    s.age=23;
    s.marks=91.00;
    printf("rollno %d\n name %s\n age %d\n marks %f",s.rollno,s.name,s.age,s.marks);
    

    return 0;
}


//--------------------------------------------------------------------------------------------------------------
//structure in C 
//Structure that takes the user input of multiple records and uses arrays to store the structure
// Online C compiler to run C program online
#include <stdio.h>
#include<string.h>
//structure in C
struct student{
    int rollno;
    char name[100];
    int age;
    float marks;
    
};
int main() {
    struct student s[5];
    int ip;
    printf("How many details you want to add?\n");
    scanf("%d",&ip);
    for(int i=0;i<ip;i++){
        printf("enter details:\n");
        scanf("%d",&s[i].rollno);
        scanf("%s",s[i].name);
        scanf("%d",&s[i].age);
        scanf("%f",&s[i].marks);
        printf("Student %d added !\n",i+1);
    }
    
    printf("student details are:\n");
    for(int i=0;i<ip;i++){
        printf("rollno %d\n name %s\n age %d\n marks %f\n",s[i].rollno,s[i].name,s[i].age,s[i].marks);
    }
    

    return 0;
}
