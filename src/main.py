from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

from pprint import pprint

python_file = open("../demos/test.py", "r")
content = python_file.readlines()
# print(content)
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
pprint(code)
myformatter = HtmlFormatter()
myformatter.lineseparator = "<br>"
# highlight(code, PythonLexer(), myformatter, open("resulting.html", "w"))
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
# print(question)
# print(algorithm)
print(code)

resulting_file = open("../cards/resulting.txt", "w")

resulting_file.write(question + "`")
resulting_file.write(algorithm + "`")
resulting_file.write(code)

resulting_file.close()
