import re

pattern = re.compile("^[A-Z][a-z]+$")
# print([pattern.search('Abbb')])
# print([pattern.search('Abbb12312312')])
# print([pattern.search('Abbasdsada')])

# file_path = "row.txt"
# with open(file_path, "r") as file:
#     file_contents = file.read()
#     # print(file_contents)

# for items in file_contents: 
#     print([pattern.search(items)])