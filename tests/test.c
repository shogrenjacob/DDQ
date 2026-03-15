// @h1 File: test.c
#include <stdio.h>

// @h2 int add(int x, int y)
// @p Add two integers
int add(int x, int y)
{
    return x + y;
}

// @h2 int sub(int x, int y)
// @p Subtract two integersLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
int sub(int x, int y)
{
    return x - y;
}

/*
@h1 Paragraph Comment
@h2 A Subheading
@p Blah blah blah
*/

// @p This is the Google Url
char* url = "https://www.google.com";

// @h2 int mult(int x, int y)
// @p Multiply two integers
int mult(int x, int y)
{
    return x * y;
}

// @h2 int div(int x, int y)
// @p Divide two integers
int div(int x, int y)
{
    return x / y;
}

// @h2 int main() - Entry Point

// This is a normal comment!
int main()
{
    // @p print "Hello world!"
    printf("Hello world!\n");

    // @a [https://jacobshogren.blog] My Blog

    // @img [./test-img.avif] Alt
}

// @p There is this link in this comment for some reason https://www.google.com

// @hr