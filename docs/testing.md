# 動作の確認

リポジトリのルートで `python main.py` を実行します。一覧に `E001` と `E002` が表示され、JSONの貸出状況と合っていることを目で確認します。

この版の確認は`tests/test_rental.py`で行います。

## テスト環境の準備
次のコマンドを実行します。
```bash
python -m pip install -r requirements.txt
```

## テスト実行
```
pytest
```

[READMEへ戻る](../README.md)
