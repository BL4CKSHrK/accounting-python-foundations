from decimal import Decimal

journal = [
    {"account": "Cash", "debit": Decimal("5000000"), "credit": Decimal("0")},
    {"account": "Accounts Receivable", "debit": Decimal("2000000"), "credit": Decimal("0")},
    {"account": "Equipment", "debit": Decimal("3000000"), "credit": Decimal("0")},
    {"account": "Accounts Payable", "debit": Decimal("0"), "credit": Decimal("2000000")},
    {"account": "Capital", "debit": Decimal("0"), "credit": Decimal("8000000")},
    # Transaksi tambahan untuk menguji ketidakseimbangan
    {"account": "Cash", "debit": Decimal("2000000"), "credit": Decimal("0")},
    {"account": "Cash", "debit": Decimal("0"), "credit": Decimal("500000")},
    {"account": "Accounts Payable", "debit": Decimal("500000"), "credit": Decimal("3000000")},
]
print("TOTAL TRANSACTION:", len(journal))


trial_balance = {}

# Define normal balance for each account 
normal_balance = {
    "Cash":"debit",
    "Accounts Receivable":"debit",
    "Equipment":"debit",
    "Accounts Payable":"credit",
    "Capital":"credit",
    "Service Revenue":"credit",
    "Rent Expense":"debit",
}

# ACCUMULATE TRANSACTIONS 
trial_balance = {}

for entry in journal:
    account = entry["account"]

    if account not in trial_balance:
        trial_balance[account] = {
            "debit": Decimal("0"),
            "credit": Decimal("0"),
        }

    trial_balance[account]["debit"] += entry["debit"]
    trial_balance[account]["credit"] += entry["credit"]

#DISPLAY AUTOMATED TRIAL BALANCE
print("AUTOMATED TRIAL BALANCE")
print("-----------------------")

for account, balances in trial_balance.items():
    print(
        f"{account:<25}: "
        f"Debit = Rp{balances['debit']:,.0f}, "
        f"Credit = Rp{balances['credit']:,.0f}"
    )

# CALCULATE TOTAL DEBIT AND CREDIT  
debit_total = sum(
    (balances["debit"] for balances in trial_balance.values()),
    Decimal("0"),
)
credit_total = sum(
    (balances["credit"] for balances in trial_balance.values()),
    Decimal("0"),
)

print("-----------------------")
print(f"{'TOTAL':<25}: Debit = Rp{debit_total:,.0f}, Credit = Rp{credit_total:,.0f}")

if debit_total != credit_total:
    print("PERINGATAN: Total debit dan kredit tidak seimbang.")
    print("STATUS: NOT BALANCED")
    print(f"Difference: Rp{abs(debit_total - credit_total):,.0f}")
else:
    print("STATUS: BALANCED")

# CALCULATE ENDING BALANCE 
print("\nENDING BALANCE")
print("-----------------------")

for account, balances in trial_balance.items():

    if normal_balance[account] == "debit":
        ending_balance = balances["debit"] - balances["credit"]

    else:
        ending_balance = balances["credit"] - balances["debit"]

    print(f"{account:<25}: Ending Balance = Rp{ending_balance:,.0f}")