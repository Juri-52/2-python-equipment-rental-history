from rental_service import RentalService
from storage import load_current_equipment, save_equipment


def show_equipment(equipment):
    if not equipment:
        print("該当する備品はありません。")
    for item in equipment:
        if item.is_available():
            status = "貸出可"
        else:
            status = f"貸出中（{item.borrower}）"
        print(f"{item.equipment_id} {item.name} / {status}")


def main():
    service = RentalService(load_current_equipment())

    while True:
        print("\n1. 一覧  2. 検索  3. 貸出  4. 返却  5. 貸出可のみ  0. 終了")
        choice = input("番号を選択: ").strip()
        try:
            if choice == "1":
                show_equipment(service.equipment)
            elif choice == "2":
                equipment_id = input("備品番号: ").strip()
                show_equipment([service.find_equipment(equipment_id)])
            elif choice == "3":
                equipment_id = input("備品番号: ").strip()
                borrower = input("利用者名: ")
                service.checkout(equipment_id, borrower)
                save_equipment(service.equipment)
                print("貸出を記録しました。")
            elif choice == "4":
                equipment_id = input("備品番号: ").strip()
                service.checkin(equipment_id)
                save_equipment(service.equipment)
                print("返却を記録しました。")
            elif choice == "5":
                show_equipment(service.get_available())
            elif choice == "0":
                break
            else:
                print("メニューにある番号を入力してください。")
        except ValueError as error:
            print(f"操作できません: {error}")


if __name__ == "__main__":
    main()
