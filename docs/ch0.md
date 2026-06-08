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

# 47th KCLC (コンピュータ部)<br>講義 Chapter 0

---

## 目次

- **競プロことはじめ**
- **ゲームを見てみよう**
- **講義を進めるにあたって**

---

## 競プロことはじめ

**まずは問題を見てみよう。**

---

## 競プロことはじめ

### 問題文

$2 \times N$ の白のマス目のいくつかのマスを、黒マスがどれも隣りあわないように黒マスをぬる方法は何通り？
答えは大きくなるので、$M$ で割った余りを求めてください。

### 制約

- $1 \leq N \leq 10^{18}$
- $2 \leq M \leq 10^{9}$
- $N, M$ は整数である。

### 小課題 (抜粋)

3. (7点) $N \leq 7$ (開成中学入試2022 算数3番)

---

## ゲームを見てみよう

**pygame** というライブラリを使用しています。(**ゲーム作成に関しては、パソコンがないと難しいので注意**)
参考: <https://python.joho.info/pygame-tutorial/>

---

## 講義を進めるにあたって

いくつか必要になるツール類があります。
可能な限り、講義が始まるまでに作っておいて欲しいです。
どれも無料。

- キーボード付きのタブレット、もしくはノートパソコン
- AtCoder <https://atcoder.jp/register>
- GitHub <https://github.com/signup>
- Google Drive <https://drive.google.com/?authuser=0>
- Google Colab <https://colab.research.google.com/?hl=ja>
