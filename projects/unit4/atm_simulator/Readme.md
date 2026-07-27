# Unit 4 Challenge – ATM Simulator

## Overview
Create a Python script called `atm_simulator.py` that simulates a bank transaction by checking if a user has enough money to withdraw.  
The program demonstrates conditional logic, type casting, and formatted output.

---

## Requirements
1. Set a fixed variable representing a bank balance, e.g. `balance = 500`.
2. Ask the user how much money they want to withdraw.  
   - Cast the input to an integer or float.
3. If the request is less than or equal to the balance:
   - Deduct the amount and print: `Withdrawal successful! Remaining balance: RX`.
4. If the request is less than or equal to 0:
   - Print: `Invalid amount. You must withdraw more than R0`.
5. Otherwise (`else`):
   - Print: `Declined. Insufficient funds`.

---

## Outcome
By completing this task, you will:
- Understand how to use conditional logic to handle multiple scenarios.
- Apply type casting to process numeric input safely.
- Simulate a simple financial transaction with error handling.
- Use f-strings for clear, formatted output.
- Build confidence in combining input, conditionals, and arithmetic in a single program.
