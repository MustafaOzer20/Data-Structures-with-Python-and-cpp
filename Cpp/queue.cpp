#include <iostream>

//queue

struct queue{
  int data;
	struct queue * next;
};

struct queue *head = NULL;
struct queue *temp = NULL;
struct queue *current = NULL;

void enqueue(int data){
  temp = (struct queue *)malloc(sizeof(struct queue));
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

int dequeue(){
  if(head == NULL){
    printf("Queue is empty");
  }
  else{
    int val = head->data;
    head = head->next;
    return val;
  }
  return -1;
}

void printQueue(){
  if(head == NULL){
    printf("Queue is empty");
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
    enqueue(i);
  }
  printQueue();
  printf("\n%d\n",dequeue());
  printQueue();

  return 0;
}