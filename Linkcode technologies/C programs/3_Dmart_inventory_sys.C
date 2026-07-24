// Online C compiler to run C program online
//Dmart inventory system
#include <stdio.h>
#include <string.h>

struct Product
{
    int id;
    char name[50];
    float price;
    int quantity;
};

struct Product p[100];
int count = 0;
void addProduct()
{
    printf("\nEnter Product ID: ");
    scanf("%d", &p[count].id);

    printf("Enter Product Name: ");
    scanf("%s", p[count].name);

    printf("Enter Product Price: ");
    scanf("%f", &p[count].price);

    printf("Enter Quantity: ");
    scanf("%d", &p[count].quantity);

    count++;

    printf("Product Added Successfully\n");
}

void viewProducts()
{
    int i;

    printf("\nID\tName\tPrice\tQuantity\n");

    for(i=0; i<count; i++)
    {
        printf("%d\t%s\t%.2f\t%d\n",p[i].id,p[i].name,p[i].price,p[i].quantity);
    }
}
void searchProduct()
{
    int id, i;

    printf("Enter Product ID to Search: ");
    scanf("%d", &id);

    for(i = 0; i < count; i++)
    {
        if(p[i].id == id)
        {
            printf("\nProduct Found\n");
            printf("ID       : %d\n", p[i].id);
            printf("Name     : %s\n", p[i].name);
            printf("Price    : %.2f\n", p[i].price);
            printf("Quantity : %d\n", p[i].quantity);

            return;
        }
    }

    printf("Product Not Found\n");
}

void updateProduct()
{
    int id, i, found = 0;

    printf("Enter Product ID to Update: ");
    scanf("%d", &id);

    for(i=0; i<count; i++)
    {
        if(p[i].id == id)
        {
            printf("Enter New Name: ");
            scanf("%s", p[i].name);

            printf("Enter New Price: ");
            scanf("%f", &p[i].price);

            printf("Enter New Quantity: ");
            scanf("%d", &p[i].quantity);

            found = 1;

            printf("Product Updated Successfully\n");
            break;
        }
    }

    if(found == 0)
    {
        printf("Product Not Found\n");
    }
}

void deleteProduct()
{
    int id, i, j;

    printf("Enter Product ID to Delete: ");
    scanf("%d", &id);

    for(i = 0; i < count; i++)
    {
        if(p[i].id == id)
        {
            for(j = i; j < count - 1; j++)
            {
                p[j] = p[j + 1];
            }

            count--;

            printf("Product Deleted Successfully\n");
            return;
        }
    }

    printf("Product Not Found\n");
}

void purchaseProduct()
{
    int id, qty, i;
    float subtotal, gst, discount, grandTotal;

    printf("Enter Product ID: ");
    scanf("%d", &id);

    for(i=0; i<count; i++)
    {
        if(p[i].id == id)
        {
            printf("Enter Quantity to Purchase: ");
            scanf("%d", &qty);

            if(qty > p[i].quantity)
            {
                printf("Insufficient Stock\n");
                return;
            }

            subtotal = qty * p[i].price;

            gst = subtotal * 0.18;

            printf("Enter Discount Amount: ");
            scanf("%f", &discount);

            grandTotal = subtotal + gst - discount;

            p[i].quantity -= qty;

            printf("\n========== BILL ==========\n");
            printf("Product: %s\n", p[i].name);
            printf("Price: %.2f\n", p[i].price);
            printf("Qty: %d\n", qty);
            printf("Subtotal: %.2f\n", subtotal);
            printf("GST(18%%): %.2f\n", gst);
            printf("Discount: %.2f\n", discount);
            printf("Grand Total: %.2f\n", grandTotal);
            printf("==========================\n");

            return;
        }
    }

    printf("Product Not Found\n");
}


int main()
{
    int choice;

    do
    {
        printf("\n=================================\n");
        printf(" DMART INVENTORY SYSTEM\n");
        printf("=================================\n");
        printf("1. Add Product\n");
        printf("2. View Products\n");
        printf("3. Search Product\n");
        printf("4. Update Product\n");
        printf("5. Delete Product\n");
        printf("6. Purchase Product\n");
        printf("7. Exit\n");

        printf("Enter Choice: ");
        scanf("%d", &choice);

        switch(choice)
        {
            case 1:
                addProduct();
                break;

            case 2:
                viewProducts();
                break;

            case 3:
                searchProduct();
                break;

            case 4:
                updateProduct();
                break;

            case 5:
                deleteProduct();
                break;

            case 6:
                purchaseProduct();
                break;

            case 7:
                printf("Thank You!\n");
                break;

            default:
                printf("Invalid Choice\n");
        }

    } while(choice != 7);

    return 0;
}

