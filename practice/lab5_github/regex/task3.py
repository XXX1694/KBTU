import re

pattern = re.compile("^[a-z]+_[a-z]+$")
# print([pattern.search('abbb_')])
# print([pattern.search('abbbb_12312312')])
# print([pattern.search('abb_asdsada')])

# file_path = "row.txt"
# with open(file_path, "r") as file:
#     file_contents = file.read()
#     # print(file_contents)

# for items in file_contents: 
#     print([pattern.search(items)])