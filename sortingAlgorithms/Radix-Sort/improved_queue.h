#ifndef _IMP_QUEUE_H
#define _IMP_QUEUE_H

typedef struct Queue
{
	int* arr;
	int arr_size;
	int size;
	int front;
	int rear;

	int (*is_full)(struct Queue* this);
	int (*is_empty)(struct Queue* this);
	int (*enqueue)(struct Queue* this, int value);
	int (*dequeue)(struct Queue* this);
} Queue;

int Queue_is_full(Queue* this)
{
	return (this->rear + 1) % this->arr_size == this->front;
}

int Queue_is_empty(Queue* this)
{
	return this->front == this->rear;
}

int Queue_enqueue(Queue* this, int value)
{
	if (this->is_full(this))
		return 0;

	int ret = this->arr[this->rear] = value;

	this->rear = (this->rear + 1) % this->arr_size;

	return ret;
}

int Queue_dequeue(Queue* this)
{
	if (this->is_empty(this))
		return 0;

	int ret = this->arr[this->front];
	this->front = (this->front + 1) % this->arr_size;

	return ret;
}

Queue* create_queue(int size)
{
	Queue* this = (Queue*)malloc(sizeof(Queue));

	this->arr = (int*)calloc(size + 1, sizeof(int));
	this->arr_size = size + 1;
	this->size = size;
	this->front = 0;
	this->rear = 0;

	this->is_empty = &Queue_is_empty;
	this->is_full = &Queue_is_full;
	this->enqueue = &Queue_enqueue;
	this->dequeue = &Queue_dequeue;

	return this;
}

void delete_queue(Queue* this)
{
	free(this->arr);
	free(this);
}

#endif
