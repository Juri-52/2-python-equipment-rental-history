from storage import load_current_equipment


def show_equipment(equipment):
    for item in equipment:
        if item.borrower is None:
            status = "貸出可"
        else:
            status = f"貸出中（{item.borrower}）"
        print(f"{item.equipment_id} {item.name} / {status}")


def main():
    equipment = load_current_equipment()
    show_equipment(equipment)


if __name__ == "__main__":
    main()
