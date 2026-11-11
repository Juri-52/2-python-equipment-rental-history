# 学校の備品管理

学校の備品を管理するアプリです。  
以下の機能があります。
- 備品の一覧表示
- 備品番号による検索
- 備品の貸出・返却
- 貸出状態の保存 - `data/current_equipment.json`に保存されます。
- 貸出可能な備品の絞り込み表示

初期データは`data/equipment.json`を読み込みます。  
`data/current_equipment.json`が存在する場合はこのファイルが読み込まれます。


## 準備と実行

動作環境：`Python 3.10`以降  
実行ディレクトリ：`2-python-equipment-rental-history`

アプリケーション本体の実行には追加パッケージは不要ですが、テストの実行には次のコマンドを実行する必要があります。
```bash
pip install -r requirements.txt
```

アプリケーション本体は、次のコマンドによって実行できます。
```bash
python main.py
```

## 詳しい説明

- [使い方](docs/usage.md)
- [データの内容](docs/data.md)
- [動作の確認](docs/testing.md)
