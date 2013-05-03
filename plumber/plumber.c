
#include "plumber.h"


#define EXCEPT_THIS_ROW	1
#define EXCEPT_THIS_COL	2
#define JUST_THIS_ROW	4
#define JUST_THIS_COL	5
#define ALL		7
#define WRITE_END	8
#define READ_END	9
#define BOTH		10


flow_matrix *array;
pid_t *pids;
int pidindex;
int flag = 1;


void muxall();
void runcommands();
void waitcommands();

void bailout();

void childhandler(int signal);
void killzombies();

void close_edges(int n, int m, int mode, int which);
void close_other_commands(int i);


#define MUX_FUNCTION collector
#define DEMUX_FUNCTION spreader

//#include "mux.c"
//#define MUX_FUNCTION mux
//#define DEMUX_FUNCTION demux

/* turning this on:
 * #define USINGCHILDHANDLER
 * causes Bad Things to happen. Don't do it.
 */


int main(int argc, char **argv)
{
	/* driver function for the plumber multipipe application */

	int i; 
	int pidcount;
	if(argc < 3){
		printf("Usage: %s [-s] <programs> -e <links>\n", argv[0]);
		printf("Options:\n	-s  Process input in sequence, rather than line by line\n");
		exit(0);
	}

#ifdef USINGCHILDHANDLER
	signal(SIGCHLD, childhandler);
#endif

	array = adj_matrix(argc, argv);

	/* we know in advance how many child processes there will be,
	 * based on the number of commands to be run (no. of edges does
	 * not affect this).
	 *
	 * this is essentially a stack of PIDs from all our forks, it
	 * pushed onto at each fork, and then all cleaned up at the 
	 * very end. Will scrapping this in favor of a SIGCHLD handler
	 * calling killzombies() do the job just as well?
	 */
	
	pidcount = 3 * array->dimension - 2;
	pids = malloc(sizeof(pid_t) * pidcount);
	pidindex = 0;

	if(pids == (int*) 0)
	{
		 perror("malloc in main");
	}

	for(i = 0; i < pidcount; ++i)
	{
		pids[i] = -1;
	}

	/* first set up all the copies of spreader and collector, 
	 * attatched to their appropriate pipes.
	 */
	
	muxall();

	/* then launch all the commands we'll need, attatched to -their- 
	 * input and output pipes.
	 */
	
	runcommands();

	/* everything went well, close all remaining FDs and clean up the PID stack
	 */

	close_other_commands(0);
	close_edges(0, 0, ALL, BOTH);
	
	waitcommands();	
	
	exit(0);

}


void muxall()
{
	int i, j;
	pid_t pid;

	/* big fat loop over every single command */
	for(i = 0; i < array->dimension; ++i)
	{
		if(i == 0)
		{
			/* special cases for command 0, which is not really a
			 * command, but instead serves as a label for both
			 * stdin and stdout. Don't actually make pipes here.
			 */
			   
			array->commandpipes[i][0][1] = 0;
			array->commandpipes[i][1][0] = 1;
		}
		else
		{
			/* normal case. create pipes.
			 */

			if(pipe(array->commandpipes[i][0]) == -1)
			{
				perror("demux pipe");
			}

			if(pipe(array->commandpipes[i][1]) == -1)
			{
				perror("mux pipe");
			}
		}
		   
		pid = fork(); /* spin off a child to run the spreader */
		
		if(pid == -1)
		{
			perror("forking demux");
		}

		if(pid == 0)
		{
			/* child branch 
			 *
			 * set up an array of file descriptors and pass it
			 * to spreader.
			 */
			
			int descriptors[array->dimension];
			
			for(j = 0; j < array->dimension; ++j)
			{
				descriptors[j] = -1;

				if(array->edges[i][j] != 0)
				{
					descriptors[j] = array->edges[i][j][1];
				}
			}

			(void) close(array->commandpipes[i][1][1]);
			close_other_commands(i);
			close_edges(i, 0, JUST_THIS_ROW, READ_END);
			close_edges(i, 0, EXCEPT_THIS_ROW, BOTH);
			
			DEMUX_FUNCTION(array->commandpipes[i][1][0], descriptors, array->dimension);
			/* this (child) MUST NOT return */
			exit(0);
		}
		/* parent continues on.. */
		
		pids[pidindex++] = pid;

		/* ... to the next fork */
		
		pid = fork(); /* spin off a child to run the collector */

		if(pid == -1)
		{
			perror("forking mux");
		}

		if(pid == 0)
		{
			/* child branch 
			 *
			 * set up an array of file descriptors and pass it to
			 * collecter.
			 */
			
			int descriptors[array->dimension];

			for(j = 0; j < array-> dimension; ++j)
			{
				descriptors[j] = -1;

				if(array->edges[j][i] != 0)
				{
					descriptors[j] = array->edges[j][i][0];
				}
			}

			(void) close(array->commandpipes[i][0][0]);
			close_other_commands(i);
			close_edges(0, i, JUST_THIS_COL, WRITE_END);
			close_edges(0, i, EXCEPT_THIS_COL, BOTH);
			
			MUX_FUNCTION(array->commandpipes[i][0][1], descriptors, array->dimension);

			/* again, this process must never return */
			exit(0);
		}
		/* parent skips to here */
		
		pids[pidindex++] = pid;
	} /* end for */
}
	

void runcommands()
{
	int i;

	/* start this loop at 1 because command 0 is not actually
	 * a program to be run. It's just a place to put standard in
	 * and standard out.
	 */

	for(i = 1; i < array->dimension; ++i)
	{
		pid_t pid;

		(void) close(array->commandpipes[i][0][1]);
		(void) close(array->commandpipes[i][1][0]);
		close_other_commands(i);
		close_edges(0, 0, ALL, BOTH);

		pid = run_redirected(array->commands[i], array->commandpipes[i][0][0], array->commandpipes[i][1][1]);

		if(pid == -1)
		{
			/* bail out: a command just failed, so we don't want to
			 * keep starting any more new ones.
			 */
			
			perror("fork in runcommands");
			bailout();
		}
		
		/* these are the pipe ends we handed off to the child, we 
		 * don't want to mess with them any more.
		 */
		
		(void) close(array->commandpipes[i][0][0]);
		(void) close(array->commandpipes[i][1][1]);
		
		pids[pidindex++] = pid;
	}
}


void waitcommands()
{
#ifndef USINGCHILDHANDLER
	int status;
	
	while(pidindex >= 0)
	{
		if(waitpid(pids[pidindex--], &status, 0) == -1)
		{
			perror("wait error");
		}
	}
#endif
}


void bailout()
{
	/* close a whole bunch of FDs so that processes reading them
	 * will terminate and get waited on.
	 */

	close_edges(0, 0, ALL, BOTH);
	close_other_commands(0);

	waitcommands();
	exit(-1);
}


void childhandler(int signal)
{
	killzombies();
}


void killzombies()
{
	while(waitpid((pid_t) -1, (int*) 0, WNOHANG) > (pid_t) -1);
}


void close_edges(int n, int m, int mode, int which)
{
	int i, j;

	void do_it()
	{
		fprintf(stderr, "closing edge: %d,%d\n", i, j);
		
		if(array->edges[i][j] != (int*) 0)
		{
			if(which == READ_END || which == BOTH)
			{
				(void) close(array->edges[i][j][0]);
			}

			if(which == WRITE_END || which == BOTH)
			{
				(void) close(array->edges[i][j][1]);
			}
		}
	}

	for(i = 0; i < array->dimension; ++i)
	{
		for(j = 0; j < array->dimension; ++j)
		{
			switch(mode)
			{
				case EXCEPT_THIS_ROW:
					
					if(i != n)
					{
						do_it();
					}
					
					break;
					
				case EXCEPT_THIS_COL:

					if(j != m)
					{
						do_it();
					}

					break;
					
				case ALL:

					do_it();

					break;
			} /* end switch */
		} /* end for: j */
	} /* end for: i */
}


void close_other_commands(int i)
{
	int index;

	void do_it()
	{
		fprintf(stderr, "closing pipes on command %d\n", index);
			
		(void) close(array->commandpipes[index][0][0]);
		(void) close(array->commandpipes[index][1][0]);
		(void) close(array->commandpipes[index][0][1]);
		(void) close(array->commandpipes[index][1][1]);
	}

	for(index = 1; index < array->dimension; ++index)
	{
		if(i != index)
		{
			do_it();
		}
	}
}

