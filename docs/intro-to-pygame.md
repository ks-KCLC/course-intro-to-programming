---
marp: true
theme: gaia
_class: lead
paginate: true
math: mathjax
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
---
<!-- markdownlint-disable MD001 -->
<!-- markdownlint-disable MD024 -->
<!-- markdownlint-disable MD029 -->
<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD036 -->
<!-- markdownlint-disable MD041 -->
<style>
section {
    font-size: 26px;
}
</style>

# 47th KCLC (コンピュータ部)<br>Pygame 講義 - 1

---

## [uv のインストール](https://docs.astral.sh/uv/getting-started/installation/)

Python をインストールするのに、uv というパッケージマネージャを通します。
仮想環境の構築にデフォルトの `venv` などより使いやすいと思います。

### Windows

PowerShell がインストールされているか確認！
[インストール方法](https://learn.microsoft.com/ja-jp/powershell/scripting/install/install-powershell-on-windows?view=powershell-7.6)

Standalone installer: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
WinGet: `winget install --id=astral-sh.uv  -e`

### Mac

Standalone installer: `curl -LsSf https://astral.sh/uv/install.sh | sh`
Homebrew: `brew install uv`

---

## uv の PATH を通す

### Windows

```pwsh
if (!(Test-Path -Path $PROFILE)) {
  New-Item -ItemType File -Path $PROFILE -Force
}
Add-Content -Path $PROFILE -Value '(& uv generate-shell-completion powershell) | Out-String | Invoke-Expression'
```

-> `where uv` で PATH が出たら OK

### Mac

`echo 'eval "$(uv generate-shell-completion zsh)"' >> ~/.zshrc`

-> `which uv` で PATH が出たら OK

---

### [Python のインストール](https://docs.astral.sh/uv/guides/install-python/)

`uv python install 3.12`
