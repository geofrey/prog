
#include "plumber.h"

flow_matrix *adj_matrix(int argc, char **argv)
{
	flow_matrix *result;
	int edge_index;
	int *commandmap;
	int i;
	
	if(argc == 1)
	{
		
#ifdef DEBUG
		perror("no arguments!");
#endif
		
		/* print usage? */
		return (flow_matrix*) 0;
	}

	edge_index = 0;
	
	while(strcmp(argv[++edge_index], "-e") != 0)
	{
		if(edge_index >= argc)
		{
			perror("required: -e marks start of edges specification");
			return (flow_matrix*) 0;
		}
	}
	
#ifdef DEBUG
	printf("start of edges found at %d\n", edge_index);
	printf("creating flow_matrix...");
#endif
	
	/* we have valid data to construct a matrix from.
	 * malloc the struct and create the data structures within
	 */
	result = malloc(1 * sizeof(flow_matrix));

	result->dimension = edge_index;
	result->commands = malloc((result->dimension) * sizeof(char*)); /* list of strings */
	result->edges = malloc(result->dimension * sizeof(int**)); /* list of rows */
	result->commandpipes = malloc(result->dimension * sizeof(int**));

	commandmap = malloc(result->dimension * sizeof(int));
	commandmap[0] = 0;
	
	for(i = 0; i < result->dimension; ++i)
	{
		int j;
		
		/* create each row */
		result->edges[i] = malloc(result->dimension * sizeof(int*));

		/* and initialize to empty */
		for(j = 0; j < result->dimension; ++j)
		{
			result->edges[i][j] = (int*) 0;
		}

		result->commands[i] = (char*) 0;

		result->commandpipes[i] = malloc(2 * sizeof(int*));
		result->commandpipes[i][0] = malloc(2 * sizeof(int));
		result->commandpipes[i][1] = malloc(2 * sizeof(int));
	}

#ifdef DEBUG
	printf("done\n");
	printf("reading commands...");
#endif

	for(i = 1; i < edge_index; ++i)
	{
		int command_number;

		if(sscanf(argv[i], "%d:", &command_number) == 1)
		{
			char *command_name;

			command_name = strchr(argv[i], ':');

			if(command_name == (char*) 0)
			{
				perror("syntax error");
				exit(ARG_ERROR);
			}
			
			command_name = &(command_name[1]); /* advance 1 character */
			
			if(result->commands[i] == (char*) 0)
			{
				result->commands[i] = malloc(strlen(command_name) * sizeof(char));
				strcpy(result->commands[i], command_name);

				commandmap[i] = command_number;

#ifdef DEBUG
				printf("\ncommand %d: %s. node label %d", i, command_name, command_number);
#endif
				
			}
			else
			{
				/* duplicate command label */

#ifdef DEBUG
				printf("\nduplicate command label . aborting.\n");
#endif
				
				exit(ARG_ERROR);
			}
		}
		else
		{
			/* parse error */

#ifdef DEBUG
			printf("\nsyntax error\n");
#endif
			
			exit(ARG_ERROR);
		}
	}

#ifdef DEBUG
	printf("...done.\n");
	printf("reading edges...");
#endif
	
	/* the command names are obtained and their labels are stored in
	 * commandmap. commandmap[index] holds the user-specified label for
	 * the index-th command in the list. (This ordering is arbitrary.)
	 */

	for(i = edge_index + 1; i < argc; ++i)
	{
		int write_label, read_label;

		if(sscanf(argv[i], "%d,%d", &write_label, &read_label) == 2)
		{
			int j;
			int write_index, read_index;

			write_index = -1;
			read_index = -1;

			for(j = 0; j < result->dimension; ++j)
			{
				/* commandmap[0] already holds 0, so this
				 * loop will properly handle the special '0'
				 * cases in edge specifications
				 *
				 * otherwise, (write|read)_index gets the same
				 * number as the index in result->commands
				 * where the corresponding command was stored.
				 */
				
				if(commandmap[j] == write_label)
				{
					write_index = j;
				}

				if(commandmap[j] == read_label)
				{
					read_index = j;
				}
			}

			if(write_index >= 0 && read_index >= 0)
			{
				result->edges[write_index][read_index] = malloc(2 * sizeof(int));
				if(pipe(result->edges[write_index][read_index]) != 0)
				{
					perror("could not create pipe");
					exit(-1);
				}

#ifdef DEBUG
				printf("\nedge: %d-->%d", write_index, read_index);
#endif
				
			}
		} /* end if sscanf... */
		else
		{
			/* parse error */

#ifdef DEBUG
			printf("\n...syntax error");
#endif
			
			exit(ARG_ERROR);
		}
	} /* end for i = 1; i < edge_index ... */

#ifdef DEBUG
	printf("...done\n");
#endif
	
	free(commandmap);
	
	return result;
	
} /* end adj_matrix */

