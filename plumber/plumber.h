
#ifndef _PLUMBER_
#define _PLUMBER

#include <stdlib.h>
#include <stdio.h>
#include <malloc.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <fcntl.h>
#include <signal.h>

int plumber_errno;

#define ARG_ERROR 1
/* #define here any other errors that might be encountered */


/* flow_matrix
 * This is the struct that describes the graph which specifies data flow
 * among the processes we are starting.
 *
 * flow_matrix->dimension: the number of commands to be run, + 1
 * 
 * flow_matrix->commands: array of strings, each string is a command line
 * ***THE FIRST ENTRY IN commands IS NOT USED***
 * 
 *  flow_matrix->edges: a directed adjacency matrix. When edges[i][j] is
 *  non-null, command i's stdout is to be connected to command j's stdin.
 *
 *  **NOTE**
 *  Since we are allowing multiple redirects of the same source/destination,
 *  there is one extra row and one extra column in the matrix.
 *  edges[0][j] == true means, the shell's stdin is to be connected to command
 *  j's stdin.
 *  edges[i][0] = true means, command i's stdout is connected to the shell's
 *  stdout.
 *  The stdout edges will normally be used only for commands which do not have
 *  their output sent to another command. I'm not sure yet under what
 *  conditions the stdin edges will be automatically turned on.
 *
 *  flow_matrix->commandpipes: array containing pipes whose ends will be
 *  dup2'd onto stdin and stdout for each command.
 *  commandpipes[i][0][0]: command i's output pipe read-end
 *  commandpipes[i][0][1]: command i's output pipe write-end
 *  commandpipes[i][1][0]: command i's input pipe read-end
 *  commandpipes[i][1][1]: command i's input pipe write-end
 *
 *  commandpipes[0][0] and commandpipes[0][1] will not be initialized
 *  to hold pipes. Instead, commandpipes[0][0][0] is set to 0 (console input)
 *  and commandpipes[0][1][1] is set to 1 (console output). No processes
 *  will be connected to read/write from commandpipes[0][0][1] or
 *  commandpipes[0][1][0]. The values there are junk.
 */

typedef struct flow_matrix
{
	int dimension;
	char **commands;
	int ***edges;
	int ***commandpipes;
} flow_matrix;

flow_matrix *adj_matrix(int argc, char **argv);
int arg_parse(char *line, char ***argvp);
pid_t run_redirected(char *commandline, int in, int out);

void spreader(int, int[], int);
void collector(int, int[], int);

//#define DEBUG

#endif
