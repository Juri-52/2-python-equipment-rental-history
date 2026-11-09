import json
import os

from equipment import Equipment

CURRENT_FILE = "data/current_equipment.json"


def load_equipment(filename: str = "data/equipment.json") -> list[Equipment]:
    with open(filename, encoding="utf-8") as file:
        rows = json.load(file)

    equipment = []
    for row in rows:
        item = Equipment(row["equipment_id"], row["name"], row["borrower"])
        equipment.append(item)
    return equipment


def load_current_equipment(filename: str = CURRENT_FILE) -> list[Equipment]:
    # 保存済みのファイルがあれば、前回の状態を読み込む。
    if os.path.exists(filename):
        return load_equipment(filename)
    return load_equipment()


def save_equipment(equipment: list[Equipment], filename: str = CURRENT_FILE) -> None:
    rows = []
    for item in equipment:
        rows.append({
            "equipment_id": item.equipment_id,
            "name": item.name,
            "borrower": item.borrower,
        })

    # 配布用のデータとは別のファイルに保存する。
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(rows, file, ensure_ascii=False, indent=2)
