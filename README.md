# JPCOAR Schema Helper

[JPCOARスキーマ](https://schema.irdb.nii.ac.jp/ja/schema) 2.0のメタデータを、YAMLを使って少しかんたんに記述できるようにするためのツールです。作成したYAMLファイルは、付属のスクリプトでJPCOARスキーマのXMLファイルに変換することができます。  
また、作成したメタデータファイルをもとに、[ResourceSync](https://www.openarchives.org/rs/1.1/resourcesync)のXMLファイルを作成することができます。

## 使い方

### 必要なソフトウェアのダウンロードとインストール

1. Pythonをインストールします。3.11以降のバージョンをインストールしてください。Windowsをお使いの場合、[MicrosoftのWebサイト](https://learn.microsoft.com/ja-jp/windows/python/beginners)にインストールや動作確認の方法が掲載されていますので、参考にしてください。
1. [Visual Studio Code](https://code.visualstudio.com/)(VSCode)をインストールします。
1. VSCodeを起動し、画面上部のメニューから「表示」→「拡張機能」を選びます。画面左側のウインドウに拡張機能の一覧が表示されるので、以下の4つに対してそれぞれ「インストール」ボタンを押します。
    * [Japanese Language Pack for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-ja)
    * [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
    * [GitHub Repositories](https://marketplace.visualstudio.com/items?itemName=github.remotehub)
    * [YAML](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml)
1. VSCodeの表示言語を切り替えます。画面上部のメニューから「表示」→」コマンド パレット」を選び、画面上部に表示されたウインドウに`display`と入力してEnterキーを押します。「日本語」を選択し、メッセージに従ってVSCodeを再起動します。

### ツールの準備

1. JPCOAR Schema Helperのファイル一式をダウンロードします。VSCodeのメニューの「表示」→「ソース管理」を選び、画面左側のウインドウの「リポジトリの複製」を選びます。画面上部のウインドウに「リポジトリ URL を指定するか、リポジトリ ソースを選択します。」と表示されますので、以下の文字列をコピーしてウインドウに入力し、Enterキーを押します。
    ```
    https://github.com/nabeta/jpcoar-schema-helper
    ```
1. 保存先のフォルダを尋ねるウインドウが表示されますので、適当なフォルダを指定します。「クローンしたリポジトリを開きますか?」というメッセージが表示されますので、「開く」を選択します。
1. VSCodeのメニューで「ファイル」→「名前をつけてワークスペースを保存」を選択し、適当なフォルダを指定して「保存」を選択します。
1. VSCodeの画面上部のメニューから「ターミナル」→「新しいターミナル」を選びます。ターミナルのウインドウが画面下部に開くので、以下のコマンドを実行して、Pythonのvenv環境をインストールします。
    ```sh
    python3 -m venv .venv
    ```
1. いったんVScodeを終了し、再起動して、VSCodeの画面上部のメニューから「ターミナル」→「新しいターミナル」を選びます。
1. ターミナルで以下のコマンドを実行して、必要なPythonのモジュールをインストールします。
    ```sh
    pip install pyyaml setuptools resync rocrate
    ```

### 動作テスト

1. Windows エクスプローラーでJPCOAR Schema Helperを保存したフォルダを開き、さらにその中にある`samples/00_sample`フォルダを開きます。`article.pdf`ファイルと`dataset.txt`ファイル、ならびにメタデータファイル`jpcoar20.yaml`が保存されていることを確認します。
1. JPCOAR Schema Helperのフォルダの中にある`public`フォルダを開き、`.well-known`というフォルダしかないことを確認します。
1. VSCodeのターミナルを開き、以下のコマンドを実行します。成功した場合は、なにも出力されません。
    ```sh
    ./jpcoar.py samples/00_sample/ https://example.com
    ```
1. 同様に、ターミナルで以下のコマンドを実行します。成功した場合は、なにも出力されません。
    ```sh
    ./resourcesync.py https://example.com
    ```
1. `public`フォルダの中に`1000`フォルダが作成され、その中に`article.pdf`ファイルと`dataset.txt`ファイル、ならびにJPCOARスキーマのXMLファイル`jpcoar20.xml`が作成されていることを確認します。
1. 同様に、`public`フォルダの中にResourceSyncのXML`capabilitylist.xml`と`resourcelist.xml`が作成されていることを確認します。

### メタデータの書き方

1. WindowsのエクスプローラーでJPCOAR Schema Helperのフォルダを開き、`work`フォルダの中に新しいフォルダを作成します。フォルダ名は資料名などわかりやすいものであれば、なんでもかまいません。ここでは`work`フォルダの中に`my_article`フォルダを作ったこととして、以降そのフォルダを`work/my_article`フォルダと記述します。
1. `samples`フォルダの中にあるサンプルのメタデータファイルから、登録する資料の種類に適したものを選んで、`work/my_article`フォルダにコピーします。ファイル名は`jpcoar20.yaml`のままとしてください。
1. `work/my_article`フォルダに、登録したい論文ファイルや研究データファイルをコピーします。ファイル名はなんでもかまいませんが、データを公開するときのURLに使用されるため、英数小文字を使用することをおすすめします。ただし、`work/my_article`フォルダの中にフォルダを作成すると、これ以降の処理が正常に動作しなくなりますので注意してください。
1. VSCodeで`jpcoar-schema-helper-main`フォルダを開きます。
1. VSCodeのファイル一覧から`work/my_article`フォルダを開き、メタデータファイル`jpcoar20.yaml`の編集と保存を行ってください。編集の際には、以下の2点に注意してください。
    - `jpcoar20.yaml`の文字コードはUTF-8としてください。VSCodeで編集する際には、特になにも設定しなくてもよいですが、メモ帳などの他のテキストエディタで編集する場合はご注意ください。
    - ファイルの1行目にある以下の記述は削除しないでください。もし削除した場合、1行目に同じ記述を追加し直してください。
      ```yaml
      # yaml-language-server: $schema=../../schema/jpcoar.json
      ```
    - ファイルの5行目にある`id`に、他のメタデータファイルと重複しない通し番号を記入してください。この番号は、データを公開するときのURLに使用されます。
      ```yaml
      id: 1001
      ```

### JPCOARスキーマのXMLへの変換　

1. VSCodeのターミナルで`jpcoar.py`スクリプトを実行し、YAMLで作成したメタデータファイルをJPCOARスキーマのXMLファイルに変換します。スクリプトを実行すると、`public`フォルダの中に`id`の番号でフォルダが作成され、そのフォルダの中にJPCOARスキーマのXMLファイル`jpcoar20.xml`と、登録する論文ファイル・研究データファイルが保存されます。
    以下のコマンドは、`work/my_article`フォルダの内容を変換する例です。コマンド文中の`https://example.com`は、実際にファイルを公開するWebサーバの名前に変更してください（テストとして実行している場合は、変更する必要はありません）。
    ```sh
    ./jpcoar.py work/my_article/ https://example.com
    ```
    メタデータの編集は`work`フォルダの中のファイルのみを用いて行います。`public`フォルダの中に作成されたファイルは編集しないでください。編集しても、再度`jpcoar.py`スクリプトを実行することで上書きされます。
1. VSCodeのターミナルで`resourcesync.py`スクリプトを実行し、ResourceSyncのXMLファイルを`public`フォルダの中に作成します。コマンド文中の`https://example.com`は、`jpcoar.py`を実行するときに指定したWebサーバの名前に変更してください（テストとして実行している場合は、変更する必要はありません）。
    ```sh
    ./resourcesync.py https://example.com
    ```
1. `public`フォルダに保存されたフォルダを、`jpcoar.py`と`resourcesync.py`で指定したWebサーバにアップロードします。

### ツールの更新

VSCodeのメニューで「表示」→「コマンド パレット」を選び、`git pull`と入力してEnterキーを押してください。「Visual Studio Codeに定期的に 「git fetch」を実行する にしますか?」というメッセージが表示された場合、「いいえ」を選択します。

### フォルダの構成

- `public`: 公開用のファイルが出力されるフォルダ
    - このフォルダに保存されたファイルは編集しないこと
- `samples`: メタデータのサンプルのフォルダ
- `schema`: メタデータスキーマの定義ファイル
- `work`: 作業用フォルダ
    - このフォルダに保存されたファイルを編集すること

### メタデータスキーマの定義ファイルの更新

この作業は開発者が行うもので、メタデータの編集では必要ありません。

1. yqコマンドをインストールします。
    ```sh
    sudo apt-get install yq
    ```
1. `schema/jpcoar.yaml`ファイルを編集します。
1. yqコマンドで`schema/jpcoar.yaml`ファイルをJSON Schemaのファイルに変換します。
    ```sh
    yq . schema/jpcoar.yaml > schema/jpcoar.json
    ```

## 作成の背景

- テキストエディタでJPCOARスキーマのメタデータを書けるようにしたい
- Pythonなどのプログラミング言語でJPCOARスキーマのメタデータを書けるようにしたい
- [JAIRO Cloud](https://jpcoar.repo.nii.ac.jp/page/42)以外の環境からメタデータを[IRDB](https://irdb.nii.ac.jp/)に送付したい
- 静的なファイルのアップロードだけでデータリポジトリを運用できるようにしたい

## TODO

- `jpcoar20.yaml`のプロパティ名を整理する
- ResourceSyncの`changelist.xml`を作成できるようにする
- [RO-Crate](https://www.researchobject.org/ro-crate/)での出力を行えるようにする
- GitHub PagesやGitLab PagesでのHTMLの出力を行えるようにする

## 作者

田辺浩介 ([@nabeta](https://github.com/nabeta))
