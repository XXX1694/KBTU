import re

pattern = re.compile("^[a].+[b]$")
# print([pattern.search('abbbb')])
# print([pattern.search('abbbb_12312312')])
# print([pattern.search('abbafsdf3435***sdsadb')])

# file_path = "row.txt"
# with open(file_path, "r") as file:
#     file_contents = file.read()
#     # print(file_contents)

# for items in file_contents: 
#     print([pattern.search(items)])