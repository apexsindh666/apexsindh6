#include<stdio.h>
typedef struct{
    float length;
    float width;
    float area;
}rectangle;
void input(int n,rectangle rect[n]);
void calculate(int n,rectangle rect[n]);
void output(int n,rectangle rect[n]);
int main()
{
    int n;
    
    printf("enter the number of rectangles:\n");
    scanf("%d",&n);
    rectangle rect[n];
    input(n,rect);
    calculate(n,rect);
    output(n,rect);
    return 0;
}
void input(int n,rectangle rect[n])
{
    for(int i=0;i<n;i++){
    printf("enter the length and width of rectangle %d\n",i+1);
    scanf("%f%f",&rect[i].length,&rect[i].width);
}
}
void calculate(int n,rectangle rect[n])
{    
    for(int i=0;i<n;i++){
    rect[i].area=rect[i].length*rect[i].width;
}}
void output(int n,rectangle rect[n])
{    
    for (int i=0;i<n;i++)
    {
    printf("the area of rectangle %d is %f\n",i+1,rect[i].area);
}
}
