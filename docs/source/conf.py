# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


import os
import sys

sys.path.insert(0, os.path.abspath("../.."))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "My Project"
copyright = "2024, mtan"
author = "mtan"

# バージョン情報、リリースとバージョンを同じにすることも可能
version = "0.1"
release = "0.1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",  # ソースコード読み込み用
    "sphinx.ext.napoleon",  # docstring パース用
    "sphinx_rtd_theme",  # Read the Docs テーマ (今回は不要*1)
    "sphinx.ext.viewcode",  # ソースコードへのリンクを追加
    "sphinx_multiversion",  # マルチバージョン用
    "sphinx.ext.autosummary",
    "sphinxcontrib.plantuml",  # sphinxcontrib.plantuml モジュールを読み込む
    "myst_parser",
    "sphinxcontrib.mermaid",
    "sphinxcontrib.openapi",
]

templates_path = ["_templates"]
exclude_patterns = [
    ".env*",
    "venv*",
    "node_modules*",
    "_build*",
    "_static*",
    "_templates*",
]

language = "ja"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}


# -- Options for sphinx-multiversion -----------------------------------------

smv_tag_whitelist = r"^\d+\.\d+\.\d+$"  # これにマッチしたタグを抽出
smv_branch_whitelist = r"^main$"  # これにマッチしたブランチを抽出

autosummary_generate = True
autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "special-members": "__init__",
    "undoc-members": True,
    "exclude-members": "__weakref__",
}

plantuml = "java -jar " + os.path.join(
    os.path.dirname(__file__), "../..", "plantuml", "plantuml.jar"
)
