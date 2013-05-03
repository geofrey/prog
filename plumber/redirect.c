
#include "plumber.h"

pid_t run_redirected(char *commandline, int in, int out)
{
	pid_t child;
	
	child = fork();

	if(child == -1)
	{
		perror("error forking");

		return -1;
	}

	if(child == 0)
	{
		char **commandargv;
		int commandargc;
		
		if(in !=0)
		{
			/* replace stdin */

			dup2(in, 0);
			(void) fcntl(in, F_SETFD, -1);
		}

		if(out != 1)
		{
			/* replace stdout */

			dup2(out, 1);
			(void) fcntl(out, F_SETFD, -1);
		}

		commandargc = arg_parse(commandline, &commandargv);

		if(execvp(commandargv[0], commandargv) == -1)
		{
			/* this happens in the child, so exiting won't clobber the program */
			exit(-1);
		}
	}

	/* closing file descriptors is left up to the calling process */

	return child;
}
