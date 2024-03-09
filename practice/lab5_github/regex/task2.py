import re

pattern = re.compile("^a{1}[b]{2,3}$")
# print([pattern.search('abbb')])
# print([pattern.search('abbbb')])
# print([pattern.search('abb')])

# file_path = "row.txt"
# with open(file_path, "r") as file:
#     file_contents = file.read()
#     # print(file_contents)

# for items in file_contents: 
#     print([pattern.search(items)])