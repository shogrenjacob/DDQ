
# TODO: Multi-line c-style comments
# TODO: Better Project Layout
# TODO: Implement more HTML elements
# TODO: Make the docs look prettier
# TODO: Maybe standalone Summary Page?
# TODO: Maybe Light / Dark mode for docs

import argparse

lines = []

DELIM = "@"

TAGS = {
    f"{DELIM}h1": "h1",
    f"{DELIM}h2": "h2",
    f"{DELIM}h3": "h3",
    f"{DELIM}h4": "h4",
    f"{DELIM}h5": "h5",
    f"{DELIM}h6": "h6",
    f"{DELIM}p": "p",
    f"{DELIM}pre": "pre",
    f"{DELIM}a": "a",
    f"{DELIM}hr": "hr",
    f"{DELIM}img": "img"
}

def parse_file(input: str):
    with open(input) as file:
        line = file.readline()

        while line != "":
            found = False
            found = parse_line(line, found)
            line = file.readline()

def parse_line(line: str, found: bool):
    for curr_char, next_char in zip(line, line[1:]):
        if curr_char == "/" and next_char == "/" and found == False and DELIM in line:
            lines.append(line)
            found = True
    
    return found

def create_doc(filename: str):
    write_doc()
    with open(f"./docs/{filename}", "w") as doc:
        doc.write(styles)
        doc.write("<div style='padding: 10px;'>")

        for line in lines:
            doc.write(line)

        doc.write("</div>")



def write_doc():
    iter = 0

    for line in lines:
        line = line.strip()
        tokens = line.split(" ")

        try:
            tag = TAGS[tokens[1]]
            lines[iter] = construct_tag(tag, tokens)
        except KeyError as e:
            print("error: " + str(e))
            break

        iter += 1

def construct_tag(tagname: str, tokens: str):
    tokens.pop(0)

    print(tokens)

    if tagname == "a":
        link = tokens[1].replace("[", "").replace("]", "")
        tokens[0] = f"<{tagname} href='{link}' target='_blank'>"
        tokens[1] = ""
        tokens.append(f"</{tagname}>\n")
        new_line = " ".join(tokens)
        print(new_line)
        return new_line
    
    if tagname == "img":
        link = tokens[1].replace("[", "").replace("]", "")
        tokens[0] = f"<{tagname} src='{link}' alt='{tokens[2]}'>"
        tokens[1] = ""
        tokens[2] = ""
        tokens.append(f"</{tagname}>\n")
        new_line = " ".join(tokens)
        print(new_line)
        return new_line

    tokens[0] = f"<{tagname}>"
    tokens.append(f"</{tagname}>\n")
    new_line = " ".join(tokens)
    print(new_line)
    return new_line

def format_doc_file_title(filename: str):
    filename = filename.replace(".","-") + ".html"
    return filename

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("file", help="Provide the path of a file to parse.")
    parser.add_argument("-t", "--theme", help="Color theme for the document (blue, red, green, black)")
    parser.add_argument("-d", "--darkmode", help="Style the doc in dark mode")

    args = parser.parse_args()

    if args.theme:
        theme = args.theme
        print(theme)
    else:
        theme = "blue"

    if args.darkmode:
        print(args.darkmode)

    styles = f"""
    <style>
    html {{
        padding: 0px;
        margin: 0px;
    }}

    body {{
        font-family: Arial, sans-serif;
        padding: 0px;
        margin: 0px;
    }}

    h1 {{
        text-decoration: underline;
        color: {theme};
    }}

    pre {{
        background-color: {theme};
    }}
    </style>

    <div style="background-color: {theme}; height: 10px;"></div>
    """

    parse_file(args.file)
    create_doc(format_doc_file_title(args.file))



'''
    f = input("Enter a file to parse: ")
    parse_file(f)
    create_doc()
'''