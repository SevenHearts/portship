#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

#define BUFSIZE 4096

int main(int argc, const char **argv) {
	int status = 1;

	if (argc != 5) {
		status = 2;
		goto exit;
	}

	FILE *i = fopen(argv[1], "rb");
	if (i == NULL) {
		perror("could not open input file");
		goto exit;
	}

	FILE *o = fopen(argv[2], "wb");
	if (o == NULL) {
		perror("could not open output file");
		goto close_i;
	}

	char *dummy = NULL;

	long offset = strtol(argv[3], &dummy, 10);
	if (offset < 0) {
		fprintf(stderr, "offset must be at least 0: %ld\n", offset);
		status = 2;
		goto close_o;
	}

	long length = strtol(argv[4], &dummy, 10);
	if (length <= 0) {
		fprintf(stderr, "length must be greater than 0: %ld\n", offset);
		status = 2;
		goto close_o;
	}

	if (fseek(i, offset, SEEK_SET) != 0) {
		perror("could not seek to input offset");
		goto close_o;
	}

	size_t nread;
	char buf[BUFSIZE];

	while (length > (signed long) sizeof(buf)) {
		nread = fread(buf, sizeof(buf), 1, i);
		if (nread != 1) {
			fprintf(stderr, "reading from input yielded unexpected eof=%d err=%d (short object count)\n", feof(i), ferror(i));
			goto close_o;
		}

		nread = fwrite(buf, sizeof(buf), 1, o);
		if (nread != 1) {
			fprintf(stderr, "writing to output yielded unexpected eof=%d err=%d (short object count)\n", feof(i), ferror(i));
			goto close_o;
		}

		length -= sizeof(buf);
	}

	/*
		NOTE: we can guarantee there will be something read here
		      since we do a greater than, NOT greater than/equals,
		      in the above while loop.
	*/

	nread = fread(buf, length, 1, i);
	if (nread != 1) {
		fprintf(stderr, "reading (final) from input yielded unexpected eof=%d err=%d (short object count)\n", feof(i), ferror(i));
		goto close_o;
	}

	nread = fwrite(buf, length, 1, o);
	if (nread != 1) {
		fprintf(stderr, "writing (final) to output yielded unexpected eof=%d err=%d (short object count)\n", feof(i), ferror(i));
		goto close_o;
	}

	status = 0; /* success! */

close_o:
	fclose(o);
close_i:
	fclose(i);
exit:
	if (status == 1) {
		/* yes, purposefully skip 2 and yes, ignore errors */
		unlink(argv[2]);
		unlink(argv[3]);
	}
	return status;
}
