
#include "plumber.h"

void print_matrix(flow_matrix *item);

int main(int argc, char **argv)
{
	flow_matrix *value;
	
	printf("bet a buck this crashes\n");
	value = adj_matrix(argc, argv);

	print_matrix(value);
	
	return 0;
}

void print_matrix(flow_matrix *item)
{
	int i;

	printf("last chance to crash - bail out now!\n");
	
	if(item == (flow_matrix*) 0)
	{
		printf("null pointer\n");
		
		return;
	}

	printf("number of commands: %d\n", item->dimension);
	printf("command list:\n");

	for(i = 0; i < item->dimension; ++i)
	{
		printf("\t%d: %s\n", i, item->commands[i]);
	}

	printf("matrix:\n");
	printf("    ");

	for(i = 0; i < item->dimension; ++i)
	{
		printf("  %2d   ", i);
	}

	printf("\n");

	for(i = 0; i < item->dimension; ++i)
	{
		int j;

		printf("%2d ", i);
		
		for(j = 0; j < item->dimension; ++j)
		{
			printf("  ");

			if(item->edges[i][j] != (int*) 0)
			{
				printf("%2d/%2d", item->edges[i][j][0], item->edges[i][j][1]);
			}
			else
			{
				printf("     ");
			}
		}

		printf("\n");
	}
}

