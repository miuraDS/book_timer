﻿# Reading Books Timer

デジタルと紙の読書時間を記録し、進捗をリアルタイムで可視化する Tkinter 製のタイマーです。開始・終了時刻とページ数を入力すると、現在どこまで読めているかを分単位で推定します。

## 主な特徴
- 開始・終了時刻とページ範囲を入力するだけで読書セッションをセットアップ
- 開始前・終了後の状態を自動判定し、残り時間や最終ページをガイド
- 1 分ごとに推定ページを自動更新
- 追加ライブラリ不要（標準 Tkinter のみ）

## 動作環境
- Python 3.10 以降推奨（Tkinter 同梱版）
- Windows 10/11 で動作確認済み

## セットアップ
```powershell
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip tk
```

## 使い方
```powershell
python book_timer.py
```
1. 開始時刻（`HH:MM`）・終了時刻・開始ページ・終了ページを入力
2. コンソールに入力内容が表示され、GUI が起動
3. 進捗ラベルに推定ページが表示され、1 分ごとに更新
4. 終了予定時刻を過ぎると「Reading session finished. Review final page …」と通知

## プロジェクト構成
```
reading_books_timer/
├─ book_timer.py      # エントリーポイント（ロジック + Tkinter UI）
├─ modules/           # 追加ロジックを切り出す場合に作成
└─ assets/            # 画像・フォント・CSV 等のリソース（必要に応じて作成）
```

- ロジック関数（時間計算やページ推定）はファイル冒頭付近にまとめ、Tkinter ウィジェット組み立ては末尾に配置する方針です。
- 新しい計算ヘルパーや設定値は `modules/` に分割し、`book_timer.py` からインポートしてください。

## 開発メモ
- コードスタイル: PEP 8（4 スペースインデント、snake_case 変数・関数、PascalCase クラス）
- ユーザーに表示する文字列は重複させず、再利用しやすく管理
- テキストは UTF-8（日本語＋英語混在可）

### テスト & 検証
- メイン: 手動検証  
  `python book_timer.py` を実行し、開始前／進行中／終了後で表示が正しいか確認
- 自動テスト（任意）: `tests/test_*.py` を追加し、計算関数を GUI から切り離して検証  
  ```powershell
  python -m pytest
  ```

## 今後のアイデア
- 休憩リマインダーの追加
- CSV やグラフへのセッション履歴エクスポート
- GUI のテーマやアイコンカスタマイズ（`assets/` フォルダ活用）

## ライセンス\n- MIT License ([LICENSE](LICENSE))

