/*includes*/
#include <stdint.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <dlfcn.h>
#include <stdio.h>
#include "API_header.h"

#define MIN_opt

#ifdef MAX_opt
#define COMP <=
#elif MIN_opt
#define COMP >=
#else
#define COMP ==
typedef struct {
	uint8_t key;
	int value;
	uint index;
	void* data;
}knoten;

knoten list[];

uint get_heap_index(knoten* self){
	return *self.index;
}

void set_heap_index(knoten* self, uint index){
	*self.index=index;
}

uint upper_index(uint index){
	return 0;
}

uint lower_index(uint index,uint cnt){
	return 0+cnt;
}

void check_heap(uint index){

	check_heap()
}

void switch_elements(uint indexA,uint indexB){
	knoten tmp=list[indexA];
	list[indexA]=list[indexB];
	list[indexB]=tmp;
}

void heapify()