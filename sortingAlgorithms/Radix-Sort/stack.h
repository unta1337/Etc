#ifndef _STACK_H
#define _STACK_H

#include <stdlib.h>

typedef struct Stack
{
	int* arr;
	int size;
	int index;

	int (*push)(struct Stack* this, int value);
	int (*pop)(struct Stack* this);
} Stack;

int Stack_push(struct Stack* this, int value)
{
	if (this->index == this->size)
		return 0;

	return this->arr[this->index++] = value;
}

int Stack_pop(struct Stack* this)
{
	if (this->index == 0)
		return 0;

	return this->arr[this->index-- - 1];
}

Stack* create_stack(int size)
{
	Stack* this = (Stack*)malloc(sizeof(Stack));

	this->arr = (int*)calloc(size, sizeof(int));
	this->size = size;
	this->index = 0;

	this->push = &Stack_push;
	this->pop = &Stack_pop;

	return this;
}

void delete_stack(Stack* this)
{
	free(this->arr);
	free(this);
}

#endif
