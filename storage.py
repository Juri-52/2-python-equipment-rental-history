import json

from equipment import Equipment


def load_equipment(filename: str = "data/equipment.json") -> list[Equipment]:
    with open(filename, encoding="utf-8") as file:
        rows = json.load(file)

    equipment = []
    for row in rows:
        item = Equipment(row["equipment_id"], row["name"], row["borrower"])
        equipment.append(item)
    return equipment
