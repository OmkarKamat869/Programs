#include<stdio.h>
struct stack{
    int top;
    int size;
    int arr[1000];
};
void push(int x, struct stack *q){
     if(q->top ==( q->size-1)){
          printf("stack is full");
          return;
     }
     q->top++;
    q->arr[q->top] = x;
}
int pop(struct stack *q){
    if(q->top == -1){
        printf("stack is empty");
        return -1;
    }
    int m;
    m = q->arr[q->top];
    q->top--;
    return m;
}
int main()
{   struct stack *q;
    q->top = -1;
    printf("enter = ");
    scanf("%d",q->size);
    q->arr[q->size];
    push(1,q);
    push(5,q);
    pop(q);
    printf("%d",q->arr[q->top]);
    return 0;

    
}