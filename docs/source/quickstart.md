# Quick start

This guide will help you get started with the project.

## Prerequisites

setup python

```sh
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

## Test

テストは各スクリプトの `if __name__ == '__main__':` 以下に記述してください。
以下のコマンドでテストを実行できます。

```sh
python ./your_script.py
```

## Overview

```{eval-rst}
.. uml::

    A -> B: request
    return response
```

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
