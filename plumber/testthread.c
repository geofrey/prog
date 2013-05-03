
#include <unistd.h>
#include <pthread.h>
#include <stdio.h>

void *printjunk(void *arg);

int main(int argc, char **argv)
{
	int threads;
	int forks;
	
	int i;

	pthread_attr_t threadmode;
	
	if(argc != 3)
	{
		return 1;
	}

	for(i = 1; i < 3; ++i)
	{
		(void) sscanf("threads=%d", &threads);
		(void) sscanf("forks=%d", &forks);
	}

	threadmode = 

	for(i = 0; i < threads; ++i)
	{
		(void) 
