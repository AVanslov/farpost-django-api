import json

with open("../scraper/farpost_author.json", "r") as authors:
    farpost_author = json.load(authors)

with open("../scraper/farpost.json", "r") as adds_data:
    farpost_adds_data = json.load(adds_data)

new_farpost_author = [author for index, author in enumerate(farpost_author) if isinstance(author["author"], str) and index <= 10]


final_data = []
for index, add in enumerate(farpost_adds_data):
    add["author"] = new_farpost_author[index]["author"]
    final_data.append(add)

with open("final_data_farpost.json", "w") as write_file:
    json.dump(final_data, write_file, ensure_ascii=False)
