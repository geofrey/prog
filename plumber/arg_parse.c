
#include "plumber.h"

static int arg_parse_rec(char *line, char ***argvp, int count);

int arg_parse(char *line, char ***argvp)
{
	int offset;
	int count;

	/* skip past any initial spaces */

	offset = 0;
	while(line[offset] == ' ')
	{
		++offset;
	}

	if(line[offset] == '\0')
	{
		*argvp = (char**) 0;
		return 0;
	}

	count = arg_parse_rec(&(line[offset]), argvp, 0);
	(*argvp)[count] = 0;
	
	return count;
}

static int arg_parse_rec(char *line, char ***argvp, int count)
{
	int offset;
	int EOW;

	int result;

	offset = 0;
	
	while(line[offset] != ' ' && line[offset] != '\0')
	{
		if(line[offset] == '"')
		{
			int quotepos = offset;

			while((line[quotepos] = line[quotepos + 1]) != '"')
			{
				if(line[quotepos] == '\0')
				{
					fprintf(stderr, "Mismatched \"\".");
					*argvp = (char**) 0;
					return 0;
				}

				++quotepos;
			}

			offset = quotepos;

			while((line[quotepos] = line[quotepos + 2]) != '\0')
			{
				++quotepos;
			}
		}
		else
		{
			++offset;
		}
	}

	EOW = offset;

	while(line[offset] == ' ')
	{
		++offset;
	}
	
	if(line[offset] == '\0')
	{
		/* end of string. Initialize array. */
		result = count + 1;
		*argvp = (char**) malloc(result * sizeof(char*));
	}
	else
	{
		/* more to go - keep recursing. */
		result = arg_parse_rec(&(line[offset]), argvp, count + 1);

		if(result == 0)
		{
			return 0;
		}
	}

	(*argvp)[count] = line;
	line[EOW] = '\0';

	return result;
}

