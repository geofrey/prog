#include "signal.h"
#include "stdio.h"
#include "unistd.h"

int flag = 1;

void handle(int signal) {
	fprintf(stdout, "WHEEEE!\n");
	flag = 0;
	
	/*
	 * The only difference I see between exit(0)ing and returning is that the 
	 * first loop down in main ticks one more time when we don't quit from the 
	 * handler. This may be a race condition, as I'm sleeping one second each 
	 * time in the child process and the parent is waiting a whole number of 
	 * seconds before signalling.
	 */
	
	/*
	exit(0);
	/*/
	return; // this is incorrect - handler should not return
	//*/
}

void setup() {
	struct sigaction foo;
	foo.sa_handler = handle;
	sigemptyset(&(foo.sa_mask));
	foo.sa_flags = 0;
	
	sigaction(SIGILL, &foo, NULL);
	sigaction(SIGFPE, &foo, NULL);
	return;
}

int main(int argc, char **argv) {
	setup();
	
	int kid;
	
	if((kid = fork()) == 0) {
		while(flag) { sleep(1); fprintf(stdout, "tick\n"); }
		fprintf(stdout, "tock\n");
		return 0;
	} else {
		sleep(5);
		kill(kid, SIGILL); // SIGILLin' like a SIGVILLAIN
		sleep(1);
		wait(kid);
	}
	
	if((kid = fork()) == 0) {
		int asplode = 5.0 / 0.0;
		fprintf(stdout, "holy cow, universe didn't end\n");
		return 0;
	} else {
		wait(kid);
	}
	
	return 0;
}
