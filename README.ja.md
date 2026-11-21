# Hokkaido の作品集

[简体中文](README.md) · [English](README.en.md) · [Español](README.es.md) · **日本語**

**[日本語で作品集を開く](https://hokkaidoooo.github.io/ja/)** · [学習ノート](https://hokkaidoooo.github.io/blog/ja/) · [GitHub プロフィール](https://github.com/Hokkaidoooo)

C++ サーバーで HTTP リクエストの流れを追い、ブラウザーでキャッシュ置換方式を比較し、サプライチェーン上のリスク波及を調べられます。各作品からリポジトリへ移動できます。資材所要量計画、オフライン閲覧ツール、マルチビーム測線計画、南京の一年分の気象記録も掲載。図には実画面・模式図・合成データの区別を明記しています。ブログには日本語の索引があり、記事本文は中国語です。

## ローカルで開く

`ja/index.html` を直接開くか、リポジトリのルートで次のコマンドを実行し、<http://127.0.0.1:4186/ja/> にアクセスします。

```sh
python -m http.server 4186 --bind 127.0.0.1
```

HTML と CSS だけの静的サイトです。JavaScript、外部フォント、アクセス解析、Cookie、フロントエンドのビルドは使いません。画像も同じサイトから読み込みます。GitHub Pages とリンク先には、それぞれの利用条件が適用されます。

## 構成と画像

- [`index.html`](index.html) に共通レイアウト、中国語原文、各プロジェクトへのリンクがあります。翻訳は [`tools/home-copy.json`](tools/home-copy.json) に収録されています。更新時は Python 3.10 以降で `python tools/localize.py` を実行し、`python tools/localize.py --check` で生成済みの 3 ページと照合できます。
- 全言語で [`assets/site.css`](assets/site.css) を共有しています。本文へのスキップリンク、キーボードのフォーカス表示、動きを抑える設定に対応。GitHub Pages は `main` のルートにあるファイルを配信します。
- [画像](assets/)は各公開プロジェクトに基づいています。システム実験室は実画面、リスク分析は合成事例、気象グラフは 2023 年の記録です。サーバー、MRP、ニュースポータルの図は模式図です。[出典と切り抜きの詳細（中国語）](README.md#图片来源)。
