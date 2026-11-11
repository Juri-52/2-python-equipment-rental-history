# データの内容

`data/equipment.json`を読み込みます。  
`data/current_equipment.json`が存在する場合は、こちらを優先して読み込みます。  
データは備品のリストです。

| キー | 内容 |
| --- | --- |
| `equipment_id` | 備品番号 |
| `name` | 備品名 |
| `borrower` | 貸出先の名前。貸出できる備品は `null` |

貸出・返却時に`data/current_equipment.json`を変更します。

[READMEへ戻る](../README.md)
