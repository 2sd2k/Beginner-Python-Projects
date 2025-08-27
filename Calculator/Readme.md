# Python Scientific Calculator (Tkinter)

A responsive, keyboard-friendly **scientific calculator** built with Python and Tkinter. Supports arithmetic, trigonometric, logarithmic, and exponential operations with **cursor-based inline editing** and a small **expression pre-processor** (e.g., `√x` → `sqrt(x)`, `^` → `**`, implicit multiplication like `2π` or `3cos(… )`).

> **Why it’s cool:** GUI + algorithms + UX. It combines a clean Tkinter interface, custom expression handling, and full keyboard support.

---

## ✨ Features

* **Scientific ops:** `sin`, `cos`, `tan`, `log` (base 10), `ln` (natural), `√`, exponents (`^`), constants `π`, `e`.
* **Expression parsing:**

  * `√(x)` → `math.sqrt(x)`
  * `a^b` → `a ** b`
  * Implicit multiplication: `2π`, `2sin(3)`, `9√(16)`, `5e^2`
* **Cursor editing:** movable caret inside the Entry display; insert/delete at the cursor.
* **Keyboard support:** numbers, operators, arrows (move cursor), **Enter** (evaluate), **Backspace** (delete), **Esc/Delete** (clear).
* **Responsive UI:** grid expands with window; buttons stretch (`sticky="nsew"`).
* **Error handling:** graceful "Error" message without crashing.



## 🧰 Tech Stack

* **Python 3.8+**
* **Tkinter** (bundled with Python on most platforms)
* **math** module

---

## 🚀 Getting Started

### 1) Clone

```bash
git clone https://github.com/<your-username>/scientific-calculator-tk.git
cd scientific-calculator-tk
```

### 2) Run

```bash
python calculator.py
```

> Tkinter comes with standard Python installers on Windows/macOS. On some Linux distros, you may need: `sudo apt-get install python3-tk`.

---

## 🎹 Keyboard Shortcuts

| Key              | Action                                |
| ---------------- | ------------------------------------- |
| `0–9`            | Insert digit                          |
| `+ - * /`        | Operators                             |
| `.`              | Decimal point                         |
| `(`, `)`         | Parentheses                           |
| `^`              | Exponent operator (converted to `**`) |
| `Enter`          | Evaluate                              |
| `Backspace`      | Delete left of cursor                 |
| `Esc` / `Delete` | Clear all                             |
| `←` / `→`        | Move cursor left/right                |

> Function buttons like **sin**, **cos**, **tan**, **log**, **ln**, **√**, **π**, **eˣ**, **xʸ** are on the GUI; you can also type letters to build function names if desired.

---

## ✅ Supported Functions & Constants

* **Arithmetic:** `+ - * /`, parentheses, decimals
* **Exponentiation:** `^` (pre-processed to `**`)
* **Roots:** `√(x)` → `sqrt(x)`
* **Trig:** `sin(x)`, `cos(x)`, `tan(x)` (radians)
* **Logs:** `log(x)` = log base 10; `ln(x)` = natural log
* **Constants:** `π` (`math.pi`), `e` (`math.e`)

> Angles are in **radians** because they use Python’s `math` module. Convert degrees with `sin(x * π/180)`.

---

## 🧠 Expression Handling Details

Before evaluation, an internal pre-processor:

* Inserts `*` where implicit multiplication is detected, e.g. `2π` → `2*π`, `3sin(5)` → `3*sin(5)`
* Rewrites `√` to `sqrt`, and `^` to `**`
* Uses a **restricted `eval`** environment: `{"__builtins__": None}` plus whitelisted math functions/constants

Example:

```
Raw:   2π + 3cos(60)
Prep:  2*π + 3*cos(60)
Eval:  uses math.pi and math.cos (radians)
```

---

## 🧯 Security Note

The app uses Python’s `eval()` with a **locked-down globals** dict and an explicit **whitelist** of math symbols. This is safer than raw `eval`, but still not a full parser. For production use, consider:

* A proper tokenizer + AST evaluator (no `eval`)
* Libraries like `asteval` or `numexpr` (trade-offs apply)

---

---

## 📦 License

MIT (or your preferred license). Add a `LICENSE` file.

---

## 🤝 Contributing

PRs welcome! Please open an issue for feature ideas or bugs.

---

## 📎 Notes

* On Linux, install Tkinter if missing: `sudo apt-get install python3-tk`.
* Trig uses radians by default; a degrees toggle is planned in the roadmap.
