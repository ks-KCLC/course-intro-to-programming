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

# 47th KCLC (コンピュータ部)<br>講義 Chapter 1

---

## 目次

- 講義の進め方
- [1.00.はじめに](https://atcoder.jp/contests/APG4bPython/tasks/APG4bPython_a)
- [1.01.出力とコメント](https://atcoder.jp/contests/APG4bPython/tasks/APG4bPython_b)
- [1.02.プログラムの書き方とエラー](https://atcoder.jp/contests/APG4bPython/tasks/APG4bPython_c)
- [1.03.四則演算と優先順位](https://atcoder.jp/contests/APG4bPython/tasks/APG4bPython_d)
- [1.04.変数と型](https://atcoder.jp/contests/APG4bPython/tasks/APG4bPython_e)
- [1.05.入力](https://atcoder.jp/contests/APG4bPython/tasks/APG4bPython_f)

---

## 講義の進め方

1. [資料置き場](https://github.com/ks-KCLC/course-intro-to-programming) にアクセス
2. [Google Colab](https://colab.research.google.com/?hl=ja) にアクセス
3. 「ノートブックを開く」ダイアログで「GitHub」を選択
4. [資料置き場](https://github.com/ks-KCLC/course-intro-to-programming)の URL (<https://github.com/ks-KCLC/course-intro-to-programming>) を入力して検索
5. 該当する講義回のノートブックをクリック (ex. `src/apg4b/ch1.ipynb`)
6. 開いたノートブック上で講義を進める

---

## 1.00.はじめに

本編: [1.00.はじめに](https://atcoder.jp/contests/APG4bPython/tasks/APG4bPython_a)

---

## 1.00.はじめに

### プログラミング言語について

- Python
- C++
- Scratch

---

## 1.00.はじめに

### プログラミング言語について

#### コンパイル言語 vs インタプリタ言語

- プログラムのパフォーマンス
  - 時間計算量
  - 空間計算量

---

## 1.00.はじめに

### プログラミング言語について

#### Python vs Scratch

<https://www.reddit.com/r/learnprogramming/comments/1ccr95z/which_is_better_to_learn_first_python_or_scratch/?tl=ja>

> Pythonから始めるのがおすすめかな。Scratchは子供とか、視覚的に学びたい人にはすごくいいんだけど、Pythonの方が現実世界での応用範囲がずっと広いし、コミュニティも大きいんだよね。それに、Web開発とかデータサイエンスとか、もっと色んなことに使える汎用性の高い言語だし。

**プログラミング言語は用途に応じて使い分けよう -> Python の用途は？**
