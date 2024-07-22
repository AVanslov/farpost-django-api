import json

with open("../scraper/farpost_author.json", "r") as authors:
    farpost_author = json.load(authors)

with open("../scraper/farpost.json", "r") as adds_data:
    farpost_adds_data = json.load(adds_data)

new_farpost_author = []
for author in farpost_author:
    if len(new_farpost_author) == 10:
        break
    elif not isinstance(author["author"], str):
        continue
    else:
        new_farpost_author.append(
            {
                "model": "api.Author",
                "pk": len(new_farpost_author) + 1,
                "fields": {"name": author["author"]},
            }
        )

with open("final_data_farpost_authors.json", "w") as write_file:
    json.dump(new_farpost_author, write_file, ensure_ascii=False)

# cформируем json для импорта авторов в соответствующую таблицу
# cформируем json для импорта объявлений в соответствующую таблицу

final_data = []
for index, add in enumerate(farpost_adds_data, start=1):
    add["author"] = index
    final_data.append(
        {
            "model": "api.Add",
            "pk": len(final_data) + 1,
            "fields": add,
        }
    )

with open("final_data_farpost_adds.json", "w") as write_file:
    json.dump(final_data, write_file, ensure_ascii=False)
