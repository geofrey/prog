
void mux(int dest, int channel[], int size)
{
	char buffer[200];
	int num;
	int i;
	int more;

	more = -1;

	while(more)
	{
		more = 0;
	
		for(i = 0; i < size; ++i)
		{
			if(channel[i] != -1)
			{
				num = read(channel[i], (void*) buffer, 200);
				if(num == 0)
				{
					(void) close(channel[i]);
					channel[i] = -1;
				}
				else
				{
					write(dest, (const void*) buffer, num);
					more = -1;
				}
			}
		}
	}

	(void) close(dest);

	return;
}

void demux(int src, int channel[], int size)
{
	char teh_char;
	int i;

	while(read(src, (void*) &teh_char, 1) == 1)
	{
		for(i = 0; i < size; ++i)
		{
			if(channel[i] != -1)
			{
				(void) write(channel[i], (const void*) &teh_char, 1);
			}
		}
	}

	for(i = 0; i < size; ++i)
	{
		if(channel[i] != -1)
		{
			(void) close(channel[i]);
		}
	}

	(void) close(src);

	return;
}
