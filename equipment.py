class Equipment:
    def __init__(self, equipment_id: str, name: str, borrower: str | None = None):
        self.equipment_id = equipment_id
        self.name = name
        self.borrower = borrower

    def checkout(self, borrower: str) -> None:
        borrower = borrower.strip()
        if not borrower:
            raise ValueError("利用者名を入力してください")
        self.borrower = borrower
