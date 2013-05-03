
# Makefile for the multipipe project

plumber_objs = plumber.o adj_matrix.o arg_parse.o redirect.o spreader.o #add files here

CFLAGS = -g -Wall

plumber : ${plumber_objs}
	gcc -o plumber ${plumber_objs}
	
testadj : testadj.o adj_matrix.o
	gcc -g -o testadj testadj.o adj_matrix.o

clean :
	rm -f *.o

remake :
	touch *.c
	make

plumber_objs : plumber.h
