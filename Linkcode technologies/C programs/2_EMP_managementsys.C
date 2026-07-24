#include <stdio.h>
#include<string.h>

int count=0;
struct Employee {

    int empid;
    char name[50];
    double salary;
    
};
struct Employee e[100];
void add_employee()
{
    printf("how many employees do u want add?\n");
    int ip;
    scanf("%d",&ip);
    for(int i=0; i<ip; i++)
    {
    printf("enter employee id \n");
    scanf("%d",&e[count].empid);
    printf("enter emp name\n");
    scanf("%s",e[count].name);
    printf("enter salary\n");
    scanf("%lf",&e[count].salary);
    printf("employee %d added !\n",count+1);
    count++;
    }
    
}

void view_emp()
{
  
    if (count==0)
    {
        printf("employee records not found!\n");
        return;
    }
    for(int i=0; i<count;i++)
    {
        printf("%d\n %s\n %.2lf\n",e[i].empid,e[i].name,e[i].salary);
    }
}

void update_emp()
{
    int id;
    printf("enter empid to update details \n");
    scanf("%d",&id);
    int found = 0;
    for(int i=0; i<count; i++)
    {
        if(id==e[i].empid)
        {
          found = 1;
          printf("1.update name\n2.update salary\n3.both\n 4.exit\n enter choice\n");
          int choice;
          scanf("%d",&choice);
          if (choice==1)
          {
              printf("enter new name\n ");
              char newname[30];
              scanf("%s",newname);
              strcpy(e[i].name,newname);
              printf("name updated !");
              printf("%d\n %s\n %.2lf\n",e[i].empid,e[i].name,e[i].salary);
              break;
          }
          else if (choice==2)
          {
              printf("enter updated salary\n ");
              double new_salary;
              scanf("%lf",&new_salary);
              e[i].salary=new_salary;
              printf("salary updated !");
              printf("%d\n %s\n %.2lf\n",e[i].empid,e[i].name,e[i].salary);
              break;
          }
          else if (choice==3)
          {
              printf("enter new name\n ");
              char newname[30];
              scanf("%s",newname);
              strcpy(e[i].name,newname);
              printf("enter updated salary\n ");
              double new_salary;
              scanf("%lf",&new_salary);
              e[i].salary=new_salary;
              printf("name and salary updated !");
              printf("%d\n %s\n %.2lf\n",e[i].empid,e[i].name,e[i].salary);
              break;
          }
          else if (choice==4)
          {
            printf("exit");
            break;
          }
          else
          {
            printf("invalid choice");
          }
        }
    }
    if(found == 0)
        {
            printf("No record found!\n");
            return;
        }
}
void total_salary()
{
    double sum=0;
    for(int i=0;i<count;i++)
    {
        sum+=e[i].salary;
    }
    printf("salary need to be paid %.2lf",sum);
}
void gross_salary()
{
    double PF;
    double HRA;
    for(int i=0;i<count;i++)
    {
        PF=e[i].salary-(e[i].salary*0.12);
        HRA=PF+(e[i].salary*0.07);
        printf("gross salary of employee %d is : %.2lf\n",e[i].empid,HRA);
    }
}
void delete_emp()
{
    int del;
    int flag=0;
    printf("Enter Id of employee which you want to delete\n");
    scanf("%d",&del);
    for(int i=0;i<count;i++)
    {
        if(del==e[i].empid)
        {
           for(int j=i;j<count;j++)
           {
            e[j]=e[j+1];
           }
           flag=1;
        }
    }
    if(flag==1)
    {
       count=count-1;
       printf("\n employee is deleted !\n");
    }  
    else{
        printf("ID not found");
    } 
}
void invoice()
{
    printf("\nEmployee_ID   Employee_Name  Employee_Salary  Deduct(PF)  Added(HRA)  In_Hand_salary\n");
    printf("|------------|---------------|----------------|-----------|-----------|---------------|\n");
    for(int i=0;i<count;i++)
    {
        printf(" %d\t\t%s\t\t%.2lf\t\t%.2lf\t\t%.2lf\t\t%.2lf\t\t\n",e[i].empid,e[i].name,e[i].salary,e[i].salary*0.12,e[i].salary*0.07,((e[i].salary-e[i].salary*0.12)+e[i].salary*0.07));
    }
}
int main() {
    int ip;
    do{
        printf("\nwelcome to EMS\n1.Add\n2.View\n3.update \n4.total salary\n5.gross salary\n6.delete\n7.view invoice\n8.exit!\nEnter yr choice:\n");
        scanf("%d",&ip);
        switch(ip)
        {
            case 1: {
                add_employee();
                break;
            }
            case 2:
            {
                view_emp();
                break;
            }
            case 3:{
                update_emp();
                break;
            }
            case 4:
            {
                total_salary();
                break;
            }
            case 5:{
                gross_salary();
                break;
            }
            case 6:{
                delete_emp();
                break;
            }
            case 7:{
                invoice();
                break;
            }
            case 8:{
                printf("exit");
                break;
            }
            default:{
                printf("invalid ip !");
            }
        }
    }
    while(ip!=8);

    return 0;
}