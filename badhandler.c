#include "signal.h"
#include "stdio.h"
#include "unistd.h"

int flag = 1;

void *handle(int signal) {
	fprintf(stdout, "WHEEEE!\n");
	flag = 0;
	return; // this is incorrect - handler should not return
}

void setup() {
	struct sigaction foo;
	foo.sa_handler = &handle;
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
