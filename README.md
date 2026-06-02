# math-intuition.jp

公開サイト：失われた数学的直観の回復  
ドメイン：math-intuition.jp  
リポジトリ名：web-math-intuition-jp

## 目的

このリポジトリは、math-intuition.jp に公開する静的Webサイトの正本です。

内部ノートやチャットで作成した草稿を、公開用に編集し、HTML / CSS / 画像などの静的ファイルとして `site/` 以下に保存します。

## 構成

```text
/
  README.md
  site/
    index.html
    assets/
      style.css
      hero-main.png
    linear-algebra-01.html
    linear-vector.html
    linear-equation-geometry.html
    linear-matrix-transform.html
    linear-basis-coordinate.html
    information-and-relation.html
    relation-form-beyond-worldness.html
  .github/
    workflows/
      deploy.yml
```

## 公開運用

`main` ブランチへ push すると、GitHub Actions が `site/` 以下をロリポップ等の公開サーバへFTPSアップロードします。

初回は `deploy.yml` の `dry-run: true` を有効にします。  
GitHub Actions のログでアップロード先・対象ファイルを確認した後、`dry-run: true` を削除して本番反映します。

## GitHub Secrets

以下を Repository Secrets に登録してください。

- `FTP_SERVER`
- `FTP_USERNAME`
- `FTP_PASSWORD`
- `SERVER_DIR`

秘密情報はリポジトリ内のファイルやチャット本文には書きません。

## 更新ルール

1. 内部ノートまたはチャット原稿を確認する
2. Web掲載用に編集・校正する
3. `site/` 以下のHTML/CSS/assetsを作成・修正する
4. 必要に応じてトップページ・目次・ナビゲーションを更新する
5. commitする
6. GitHub Actionsで自動反映する

FTPでの手動アップロードは原則行いません。
