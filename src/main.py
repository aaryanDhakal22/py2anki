from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

# Input
PATH_TO_TARGETED_FILE = None  # STRING

# Output
PATH_TO_CARD_FILE = None  # STRING

python_file = open(PATH_TO_TARGETED_FILE, "r")
content = python_file.readlines()

question = str()
algorithm = str()
complexity = str()
code = str()

counter = 0

for n, i in enumerate(content):
    if i != "\n":
        if counter == 0:
            question += i[2:-1]
        if counter == 1:
            algorithm += i[2:-1] + " "
        if counter == 2:
            complexity += i[2:-1] + ";"
        if counter == 3:
            for i in content[n:]:
                code += i
            break
    else:
        counter += 1

myformatter = HtmlFormatter()
myformatter.lineseparator = "<br>"

code = highlight(code, PythonLexer(), myformatter)
code = (
    "<table class="
    "highlighttable"
    "><tbody><tr><td>" + code[:-1] + "</td></tr></tbody></table><br>"
)

algorithm += (
    "<br>"
    + "The time and space complexities are <i>"
    + ", ".join(complexity.split(";")[:-1])
    + "</i>respectively."
)
print(code)

resulting_file = open(PATH_TO_CARD_FILE, "w")
resulting_file.write(question + "`")
resulting_file.write(algorithm + "`")
resulting_file.write(code)

resulting_file.close()
