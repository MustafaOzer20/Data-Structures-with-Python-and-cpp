#include <iostream>

//stack

struct stack{
  int data;
	struct stack * next;
};

struct stack *head = NULL;
struct stack *temp = NULL;
struct stack *current = NULL;

void push(int data){
  temp = (struct stack *)malloc(sizeof(struct stack));
  temp->data = data;
  temp->next = NULL;

  if(head == NULL){
    head = temp;
  }
  else{
    current = head;
    while(current->next != NULL){
      current = current->next;
    }
    current->next = temp;
  }
}

int pop(){
  if(head == NULL){
    printf("Stack is empty");
  }
  else{
    temp = head;
    while(temp->next != NULL){
      current = temp;
      temp = temp->next;
    }
    int val = temp->data;
    free(temp);
    current->next = NULL;
    return val;
  }
  return -1;
}

void printStack(){
  if(head == NULL){
    printf("Stack is empty");
  }
  else{
    temp = head;
    while(temp->next != NULL){
      printf("%d->", temp->data);
      temp = temp->next;
    }
    printf("%d", temp->data);
  }
}

int main() {
  for(int i = 0; i < 10; i++){
    push(i);
  }
  pop();
  printStack();

  return 0;
}