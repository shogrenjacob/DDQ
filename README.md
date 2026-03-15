# Docs Done Quick (DDQ)
Docs Done Quick DDQ is a command line tool for rapidly generating code-level documentation by simply adding specially formatted comments within your source code. DDQ is language-agnostic, and compiles an HTML document with the generated documentation.

## Installation

## Usage
Simply add a delimited HTML tag to an single-line comment in your source code!

```c
// @h1 Hello World Program

// @h2 Entry-point to the program
int main()
{
    // @p Prints "Hello World!" to the console.
    printf("Hello World!\n");
}
```

Once you're done commenting your code, run the following command from this source directory:
``` python main.py <path-to-your-source-code>```



## List of Supported Languages
- C
- C++
- Java
- C#
- JavaScript
- TypeScript
