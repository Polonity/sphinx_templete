# Sphinx templete

Sphinx でドキュメントを作成する際のテンプレートです。

[Sphinxとは](https://zenn.dev/y_mrok/books/sphinx-no-tsukaikata)

本テンプレートを組み込むと、以下の機能が利用可能になります。

- sphinx によるドキュメント作成
- github actions による自動ビルド & github pages へのデプロイ

## Quick Start

プロジェクトに組み込む場合、以下のファイルをコピーしてください。

```sh
cd tmp
git clone https://github.com/Polonity/sphinx_templete.git
cp -fr .github ../
cp -fr docs ../
cp -fr requirements.txt ../
cp -fr refresh_pydoc.sh ../
cp -fr how_to_write_documentation.md ../

```

例えば、以下のようなドキュメントを作成することができます。

- システム全体の外部仕様
  - markdown で記述
  - marmaid や plantuml で図を描画可能。但し、sphinx の拡張機能で読み込めるように記載が必要。
    __記載例__
    __plantuml__
    ```md
    ```{eval-rst}
    .. uml::

        A -> B: request
        return response
    ```
    ```
    ```plantuml
    @startuml
        A -> B: request
        return response
    @enduml
    ```

    __mermaid__
    ```md    
    ```{eval-rst}
    .. mermaid::

        sequenceDiagram
            participant Alice
            participant Bob
            Alice->John: Hello John, how are you?
            loop Healthcheck
                John->John: Fight against hypochondria
            end
            Note right of John: Rational thoughts <br/>prevail...
            John-->Alice: Great!
            John->Bob: How about you?
            Bob-->John: Jolly good!
    ```

    ```

    ```mermaid
    sequenceDiagram
        participant Alice
        participant Bob
        Alice->John: Hello John, how are you?
        loop Healthcheck
            John->John: Fight against hypochondria
        end
        Note right of John: Rational thoughts <br/>prevail...
        John-->Alice: Great!
        John->Bob: How about you?
        Bob-->John: Jolly good!
    ```

- 関数の外部仕様
  - 関数冒頭に Google スタイルの docstring を仕込むと、それを自動的にドキュメント化。
    __記載例__

    ```python
    def func(arg1: int, arg2: str) -> bool:
        """[summary]

        Note:
            [description]
        Args:
            arg1 (int): [description]
            arg2 (str): [description]

        Returns:
            bool: [description]

        Any additional information.
        """
    ```

- クラスの外部仕様
  - クラス冒頭に Google スタイルの docstring を仕込むと、それを自動的にドキュメント化。
    __記載例__

    ```python
    class MyClass:
        """[summary]

        Note:
            [description]
        """
    ```

- API gateway の API仕様
  - OpenAPI 3.0 で AWS API Gateway の API 仕様をエクスポートし、それをドキュメント化。
    __記載例__

    ```rest
    .. openapi:: openapi.yml
    ```

## Quick Start

### package

```sh
apt update 
apt install -y default-jre openjdk-17-jdk graphviz 
```

### plantuml

plantuml/plantuml.jar に配置しているが、適宜アップデートする。

### python

```sh
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

### sphinx

```sh
sphinx-quickstart docs
> Separate source and build directories (y/n) [n]: y

# docs/source ディレクトリに source ディレクトリをコピー
cp -r source/* docs/source/
```

以下のようなディレクトリ構成でドキュメントが生成される。

```txt
docs/
├── make.bat
├── Makefile
└── source
    ├── _static
    ├── _templates
    ├── conf.py
    └── index.rst
```

## ドキュメントのビルド

```sh
cd docs
make html
```

## ドキュメントのホットリロード

```sh
sphinx-autobuild source/ ./build/html   # ブラウザでリアルタイムに変更を確認できる
sphinx-autobuild source/ ./build/html --port 8008  # ポート指定
```

## ドキュメント構成の設定

あなたのプロジェクトに合わせて、以下のファイルを変更してください。

### プロジェクト名を変更

`My Project` というプロジェクト名で設定してあるので、
これを grep などで置換してください。

### python モジュールのパスを変更

`docs/source/conf.py` の以下の行を変更してください。

```python
sys.path.insert(0, os.path.abspath('../..'))
```

`../..` はプロジェクトのルートディレクトリを指しています。

### favicon の変更(任意)

`docs/source/favicon.ico` を変更してください。

### API 仕様の変更

./docs/source/openapi.yml を変更すると、自動的にドキュメントが更新される。

### ドキュメントにする python モジュールを追加

#### 自動収集

以下のコマンドでプロジェクト内の python モジュールを自動収集する。
⚠️ `docs/source/auto_generated_*` はスクリプトで自動生成されるため、手動で編集しないこと。

```sh
./refresh_pydoc.sh
```

自動生成したドキュメントは以下のファイルに追加される。

```sh
docs/source/auto_generated_[python_base_dir].rst
```

例えば、以下のようなファイルの場合、

```txt
your_lambda_function_src_path/your_lambda_function.py
```

以下のrst が自動生成され、module が追加される。

```txt
docs/source/auto_generated_your_lambda_function_src_path.rst
```

#### 手動追加

例えば、以下のpython ファイルをドキュメントとして追加する。

```txt
your_lambda_function_src_path/your_lambda_function.py
```

表示したい docs/source/*.rst に追加する。

```diff
    .. autosummary::
        :toctree: generated
        :recursive:
        
+        your_lambda_function

```

以上を設定後、 `make html` でドキュメントが更新される。
