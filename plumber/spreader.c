#include "plumber.h"
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <sys/time.h>
#include <unistd.h>

extern int flag;

void spreader( int read_from, int array[], int size );

void collector( int write_to, int array[], int size );

//changed this so the project will build
int tmain()
{
//	int f1 = open( "f1", O_RDWR );
//	int f2 = open( "f2", O_RDWR );
//	int f3 = open( "f3", O_RDWR );

//	int a[5];
//	a[0] = f1;
//	a[1] = -1;
//	a[2] = f2;
//	a[3] = -1;
//	a[4] = f3;

//	collector( 1, a, 5 );
   //spreader( 0, a, 5);
	
	int a[5];
	a[0] = -1;
	a[1] = -1;
	a[2] = -1;
	a[3] = -1;
	a[4] = -1;

	int b[2];

	pipe( b );
	
	int pid = fork();

	collector(1, a, 5);
	if( pid == 0)
	{
	   close(b[0]);
		dup2( b[1], 1);

//		execv("who\0");
	}
	else
	{
			  close(b[1]);
	}
	
	return 0;
}

/* this function take a fd that it will read from and a array of size
 * that will contain fd's that will all be written each char read.
 * every element of array that isn't -1 is a fd */
void spreader( int read_from, int array[], int size )
{
	char c;

	/* read from the in pipe and write to all of the out pipes */
	while( read( read_from, &c, 1 ) != 0 )
	{
		int i;
		for( i = 0; i < size; i++ )
		{
			if( array[i] != -1 )
			{
				write( array[i], &c, 1 );
			}//end if
		}//end for
	}//end while

	/* no more to read (i.e. read pipe closed).  close all out pipes */
	int i;
	for( i = 0; i < size; i++ )
	{
		if( array[i] != -1 )
		{
			close( array[i] );
		}//end if
	}//end for
}//end spreader

void collector( int write_to, int array[], int size )
{
	fd_set rfds;
	int max_fd;
	int open_pipes = 0;

	do
	{
		FD_ZERO( &rfds );
		max_fd = 0;

		/* fill up the fd_set for select */
		int i;
		for( i = 0; i < size; i++ )
		{
			if( array[i] != -1 )
			{
		  	  open_pipes++;
				FD_SET( array[i], &rfds );
				if( array[i] > max_fd )
				{
					max_fd = array[i];
				}//end if
			}//end if
		}//end for

		printf("open pipes: %d\n", open_pipes);
		if(open_pipes == 0)
		{
				  printf("2nd close write to, return\n");
				  close(write_to);
				  return;
		}
		
		/* do select */
		int ava_reads;
		ava_reads = select( max_fd + 1, &rfds, NULL, NULL, NULL );

		/* deal with reads */
		for( i = 0; i < size; i++ )
		{
			if( array[i] != -1 )
			{
				if( FD_ISSET( array[i], &rfds ) != 0 )
				{
					if( flag == 1 )
					{
					   /* read one line before doing select again */
						char c;
						int x;

						do
						{
//printf("read from %d\n", array[i]);
						   x = read( array[i], &c, 1 );

							if( x != 0 )
							{
							   write( write_to, &c, 1 );
							}//end if
							else
							{
							   array[i] = -1;
							}//end else
						} while( c != '\n' && x != 0 );//end while

					}//end if
					else
					{
					   /* read until pipe closes, then do select again */
					   char c;
						
						while( read( array[i], &c, 1 ) != 0 )
						{
					   	write( write_to, &c, 1 );
						}//end while

						array[i] = -1;
					}//end else
				}//end if
			}//end if
		}//end for

		/* count number of open pipes */
		open_pipes = 0;
		int j;
		for( j = 0; j < size; j++ )
		{
	      if( array[j] != -1 )
         {
		      open_pipes++;
		   }//end if
		}//end for
	} while( open_pipes > 0 );//end do
printf("close write_to\n");
	/* close write_to pipe */
	close( write_to );
}//end collector function
