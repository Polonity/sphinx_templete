

"""
docstring での記述方法を示すためのサンプルコードです。
=======================================================

このページの目的は、docstring での記述方法を示すことです。
このページは、以下のソースコードから自動生成されています。

.. function::how_to_write_documentation

注釈
----------------------------------------------------

.. note::
    注釈を記述するためのサンプルです。
    
.. code-block:: rst
        
    .. note::
        注釈を記述するためのサンプルです。

警告
----------------------------------------------------

.. warning::
    警告を記述するためのサンプルです。
    
.. code-block:: rst

    .. warning::
        警告を記述するためのサンプルです。
        
        
参考
----------------------------------------------------

.. seealso::
    参考情報を記述するためのサンプルです。
    
.. code-block:: rst

    .. seealso::
        参考情報を記述するためのサンプルです。
        
このバージョンで追加された機能を書くとき
----------------------------------------------------

.. versionadded:: 1.0.0
    このバージョンで追加された機能です。
    
.. code-block:: rst

    .. versionadded:: 1.0.0
        このバージョンで追加された機能です。
        
このバージョンで変更された機能を書くとき
----------------------------------------------------

.. versionchanged:: 1.0.0
    このバージョンで変更された機能です。
    
.. code-block:: rst

    .. versionchanged:: 1.0.0
        このバージョンで変更された機能です。
        
このバージョンで非推奨された機能を書くとき
----------------------------------------------------

.. deprecated:: 1.0.0
    このバージョンで非推奨となった機能です。
    
.. code-block:: rst

    .. deprecated:: 1.0.0
        このバージョンで非推奨となった機能です。
        
        
ラベル
----------------------------------------------------

.. rubric:: ラベル

.. code-block:: rst

    .. rubric:: ラベル
        
コードブロック
----------------------------------------------------

.. code-block:: python
        
        print("Hello, World!")

.. code-block:: rst

    .. code-block:: python
            
            print("Hello, World!")

        
語録
----------------------------------------------------

.. glossary::

    term
        This is term.

    term2
        This is term2.

.. code-block:: rst

    .. glossary::

        term
            This is term.

        term2
            This is term2.
        
リンクを貼る場合
----------------------------------------------------

.. seealso::
    他のモジュールに関連する情報を記述するためのサンプルです。
    `Google`_

.. _Google: https://www.google.com

    
.. code-block:: rst

    .. seealso::
        他のモジュールに関連する情報を記述するためのサンプルです。
        `Google`_

    .. _Google: https://www.google.com


画像
----------------------------------------------------

※画像を docs/source/_static フォルダに保存してください。

.. image:: /_static/sample.png

.. code-block:: rst

    .. image:: /_static/sample.png



Plant UML
----------------------------------------------------

.. uml::
    :scale: 50 %
    :align: center

        actor User

        User -> Form : Input user information
        activate Form
        Form -> Database : Register user information
        activate Database
        Form <- Database : Inform success
        deactivate Database
        User <- Form : Show success message
        deactivate Form


.. code-block:: rst

    .. uml::
        :scale: 50 %
        :align: center

            actor User

            User -> Form : Input user information
            activate Form
            Form -> Database : Register user information
            activate Database
            Form <- Database : Inform success
            deactivate Database
            User <- Form : Show success message
            deactivate Form


Mermaid Diagram
----------------------------------------------------

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

.. code-block:: rst

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

        
"""

# classes
class MyClass:
    """
    This is a class for simple example.
    
    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
    
    """
    
    def __init__(self, name: str, age: int):
        """
        The constructor for MyClass class.
        
        Parameters:
            name (str): The name of the person.
            age (int): The age of the person.
        """
        self.name = name
        self.age = age
        
    def say_hello(self):
        """
        This method greets the person.
        
        Returns:
            str: Greeting message.
        """
        return f"Hello, {self.name}!"


# functions
def my_function(param1: int, param2: str) -> str:
    """
    This is a function for simple example.
    
    Parameters:
        param1 (int): The first parameter.
        param2 (str): The second parameter.
        
    Returns:
        str: The return value.
    """
    return f"{param1}: {param2}"

# variables
my_variable = "This is a variable."
my_variable2 = 1000
my_variable3 = MyClass("mtan", 20)
my_variable4 = my_function(1, "test")
