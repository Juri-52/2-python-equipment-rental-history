class Equipment:
    def __init__(self, equipment_id: str, name: str, borrower: str | None = None):
        self.equipment_id = equipment_id
        self.name = name
        self.borrower = borrower
