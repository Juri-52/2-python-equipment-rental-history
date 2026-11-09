class Equipment:
    def __init__(self, equipment_id: str, name: str, borrower: str | None = None):
        self.equipment_id = equipment_id
        self.name = name
        self.borrower = borrower

    def is_available(self) -> bool:
        return self.borrower is None

    def checkout(self, borrower: str) -> None:
        borrower = borrower.strip()
        if not borrower:
            raise ValueError("利用者名を入力してください")
        if not self.is_available():
            raise ValueError("この備品は貸出中です")
        self.borrower = borrower

    def checkin(self) -> None:
        if self.is_available():
            raise ValueError("この備品は貸し出されていません")
        self.borrower = None
