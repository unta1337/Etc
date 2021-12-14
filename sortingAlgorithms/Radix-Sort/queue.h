#ifndef _QUEUE_H
#define _QUEUE_H

#include "stack.h"

typedef struct Queue
{
	Stack* front_stack;
	Stack* back_stack;
	int size;
	int index;

	int (*enqueue)(struct Queue* this, int value);
	int (*dequeue)(struct Queue* this);
} Queue;

int Queue_enqueue(Queue* this, int value)
{
	if (this->front_stack->index == this->front_stack->size)
		return 0;

	int ret = this->front_stack->push(this->front_stack, value);
	this->index = this->front_stack->index;

	return ret;
}

int Queue_dequeue(Queue* this)
{
	if (this->front_stack->index == 0)
		return 0;

	while (this->front_stack->index != 0)
		this->back_stack->push(this->back_stack, this->front_stack->pop(this->front_stack));

	int ret = this->back_stack->pop(this->back_stack);

	while (this->back_stack->index != 0)
		this->front_stack->push(this->front_stack, this->back_stack->pop(this->back_stack));

	this->index = this->front_stack->index;

	return ret;
}

Queue* create_queue(int size)
{
	Queue* this = (Queue*)malloc(sizeof(Queue));

	this->front_stack = create_stack(size);
	this->back_stack = create_stack(size);
	this->size = size;
	this->index = 0;

	this->enqueue = &Queue_enqueue;
	this->dequeue = &Queue_dequeue;

	return this;
}

void delete_queue(Queue* this)
{
	delete_stack(this->front_stack);
	delete_stack(this->back_stack);
	free(this);
}

#endif
