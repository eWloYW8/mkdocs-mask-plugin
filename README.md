# Mkdocs Mask Plugin

A MkDocs plugin that adds a custom `!mask[...]` syntax to hide text behind a black box until hovered.

## Install

```bash
pip install mkdocs-mask-plugin
```

[![Build and Release](https://github.com/eWloYW8/mkdocs-mask-plugin/actions/workflows/release.yml/badge.svg)](https://github.com/eWloYW8/mkdocs-mask-plugin/actions/workflows/release.yml)

## Usage

### 1. Enable the Plugin

In your `mkdocs.yml` configuration file, add the plugin:

```yaml
plugins:
  - mask
```

### 2. Use the `!mask[...]` Syntax in Markdown

In any Markdown (`.md`) file, wrap the sensitive or hidden text using the `!mask[...]` syntax:

```markdown
Do not reveal this unless you're ready: !mask[This is a hidden message].
```

This will render as a **black box** that hides the text until the user hovers over it.

---

### 3. Resulting Behavior

The masked content will appear as a blacked-out block like this:

```
Do not reveal this unless you're ready: ██████████████████
```

When the user hovers their mouse over it, the black box fades away and the original text is revealed with a smooth transition.

