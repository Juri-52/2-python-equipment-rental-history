import pytest

from equipment import Equipment
from rental_service import RentalService
from storage import load_current_equipment, save_equipment


def test_find_equipment():
    equipment = Equipment("E001", "ノートPC")
    service = RentalService([equipment])

    assert service.find_equipment("E001") is equipment
    with pytest.raises(ValueError, match="見つかりません"):
        service.find_equipment("E999")


def test_checkout_and_return():
    equipment = Equipment("E001", "ノートPC")
    service = RentalService([equipment])

    service.checkout("E001", "田中")
    assert equipment.borrower == "田中"
    assert not equipment.is_available()

    service.checkin("E001")
    assert equipment.is_available()


def test_second_checkout_keeps_first_borrower():
    equipment = Equipment("E001", "ノートPC", "田中")
    service = RentalService([equipment])

    with pytest.raises(ValueError, match="貸出中"):
        service.checkout("E001", "佐藤")

    assert equipment.borrower == "田中"


def test_checkout_requires_borrower_name():
    equipment = Equipment("E001", "ノートPC")
    service = RentalService([equipment])

    with pytest.raises(ValueError, match="利用者名"):
        service.checkout("E001", "  ")

    assert equipment.is_available()


def test_return_requires_existing_loan():
    service = RentalService([Equipment("E001", "ノートPC")])

    with pytest.raises(ValueError, match="貸し出されていません"):
        service.checkin("E001")


def test_list_available_equipment():
    camera = Equipment("E003", "デジタルカメラ")
    computer = Equipment("E001", "ノートPC", "田中")
    service = RentalService([camera, computer])

    assert service.get_available() == [camera]


def test_reload_saved_equipment(tmp_path):
    # tmp_pathは、pytestがテスト用に作る一時フォルダー。
    filename = str(tmp_path / "current_equipment.json")
    equipment = Equipment("E001", "ノートPC")
    service = RentalService([equipment])

    service.checkout("E001", "田中")
    save_equipment(service.equipment, filename)
    reloaded = RentalService(load_current_equipment(filename))
    assert reloaded.find_equipment("E001").borrower == "田中"

    reloaded.checkin("E001")
    save_equipment(reloaded.equipment, filename)
    assert load_current_equipment(filename)[0].is_available()
