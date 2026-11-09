from equipment import Equipment


class RentalService:
    def __init__(self, equipment: list[Equipment]):
        self.equipment = equipment

    def find_equipment(self, equipment_id: str) -> Equipment:
        for item in self.equipment:
            if item.equipment_id == equipment_id:
                return item
        raise ValueError("指定した番号の備品が見つかりません")
