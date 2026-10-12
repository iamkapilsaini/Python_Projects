# Python ATM Simulator 💳

A command-line ATM simulation built with Python. This project demonstrates fundamental Python programming concepts, including functions, loops, conditional statements, modules, and file handling for persistent balance storage.

https://github.com/user-attachments/assets/7a0e3d8b-3662-4526-9797-57958b2622b4


## ✨ Features

- **PIN Authentication:** Login with a PIN and a maximum of 3 attempts.
- **Check Balance:** View the current account balance.
- **Deposit Money:** Deposit money and update the saved balance.
- **Withdraw Money:** Withdraw money only when sufficient funds are available.
- **Transaction History:** Maintain separate lists of successful deposits and withdrawals.
- **Persistent Storage:** Save account data in a JSON file so the balance remains available after the program closes.
- **Input Validation:** Reject invalid menu choices and non-positive transaction amounts.

## 🛠️ Technologies Used

- Python 3
- JSON
- VS Code

## 📁 Project Structure

```text
Python-ATM-Simulator/
├── main.py       # PIN authentication and ATM menu
├── function.py   # Balance, deposit, and withdrawal functions
├── record.py     # Load and save account records
├── record.json   # Persistent account data
└── README.md     # Project documentation
```

## 🚀 How to Run

1. Install Python 3.
2. Clone or download this repository.
3. Open the project folder in VS Code.
4. Run the following command in the terminal:

   ```bash
   python main.py
   ```

5. Enter the configured PIN to access the ATM menu.

## 💰 How It Works

The program uses three main operations to manage the balance:

1. **Load:** Read the saved account data from `record.json`.
2. **Update:** Add a deposit or subtract a valid withdrawal from the current balance.
3. **Save:** Write the updated balance and transaction records back to `record.json`.

### Example

| Operation | Amount | Balance |
|---|---:|---:|
| Initial balance | — | ₹0 |
| Deposit | ₹5,000 | ₹5,000 |
| Withdrawal | ₹2,000 | ₹3,000 |
| Deposit | ₹1,000 | ₹4,000 |

## 📚 Python Concepts Practiced

- Variables and data types
- `if`, `elif`, and `else`
- `for` and `while` loops
- Functions and function calls
- Modules and imports
- Lists and dictionaries
- File handling with `open()`
- JSON serialization and deserialization
- Exception handling with `try` and `except`

## 🔮 Future Improvements

- Hide PIN input while typing.
- Handle non-numeric input without crashing.
- Add transaction dates and timestamps.
- Add PIN changes and multiple user accounts.
- Display a detailed transaction history.
- Add a graphical user interface (GUI).

## ⚠️ Disclaimer

This is an educational project intended to practise Python programming. It is not a real banking application and does not implement production-grade authentication or financial security.

## 👨‍💻 Author

**Kapil Saini**

A beginner Python project developed as part of my programming and cybersecurity learning journey.
