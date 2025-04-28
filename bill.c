#include<stdio.h>
typedef struct{
    int consumerid;
    float units;
    float billamount;
}bill;
void input(int n,bill bills[n]);
void calculatebill(int n,bill bills[n]);
bill highest(int n,bill bills[n]);
void output(bill b);
int main()
{
    int n;
    printf("enter the number of consumer:\n");
    scanf("%d",&n);
    bill bills[n];
    input(n, bills);
    calculatebill(n, bills);
   bill b= highest(n, bills);
    output(b);
    return 0;
}
void input(int n,bill bills[n])
{
    for(int i=0;i<n;i++){
        printf("enter the details of consume %d\n",i+1);
        printf("enter the consumer ID\n");
        scanf("%d",&bills[i].consumerid);
        printf("units consumed\n");
        scanf("%f",&bills[i].units);
    }
}
void calculatebill(int n,bill bills[n])
{
    for(int i=0;i<n;i++){
        bills[i].billamount=bills[i].units*10;
    }
}
bill highest(int n,bill bills[n])
{   
     int highest=0;
    for(int i=0;i<n;i++)
    {
        if (bills[i].billamount>bills[highest].billamount)
        {
            highest=i;
        }
    }return bills[highest];
}
void output(bill b){
    printf("electricity bill details\n");
    printf("consumer ID: %.2d\n",b.consumerid);
    printf("bill amount =%.2f\n",b.billamount);
}
