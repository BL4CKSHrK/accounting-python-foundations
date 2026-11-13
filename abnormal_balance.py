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

    # Define normal balance for each account
normal_balance = {
    "Cash": "debit",
    "Accounts Receivable": "debit",
    "Equipment": "debit",
    "Accounts Payable": "credit",
    "Capital": "credit",
    "Service Revenue": "credit",
    "Rent Expense": "debit",
}

trial_balance = {}

# CREATE SEPARATE TEST DATASET
journal_test = [entry.copy() for entry in journal]

# CREATE ABNORMAL BALANCE SCENARIO
for entry in journal_test:
    if (
        entry["account"] == "Accounts Payable"
        and entry["debit"] == Decimal("500000")
    ):
        entry["debit"] = Decimal("6000000")  

# CREATE ZERO BALANCE SCENARIO
journal_test.extend([
    {
        "account": "Rent Expense",
        "debit": Decimal("1000000"),
        "credit": Decimal("0"),
    }, 
    {
        "account": "Rent Expense",
        "debit": Decimal("0"),
        "credit": Decimal("1000000"),
    }
])

# ACCUMULATE TRANSACTIONS
for entry in journal_test:
    account = entry["account"]

    if account not in trial_balance:
        trial_balance[account] = {
            "debit": Decimal("0"),
            "credit": Decimal("0"),
        }

    trial_balance[account]["debit"] += entry["debit"]
    trial_balance[account]["credit"] += entry["credit"]

# DISPLAY AUTOMATED TRIAL BALANCE
print("AUTOMATED TRIAL BALANCE")
print("-----------------------")

for account, balances in trial_balance.items():
    print(
        f"{account:<25}: "
        f"Debit = Rp{balances['debit']:,.0f}, "
        f"Credit = Rp{balances['credit']:,.0f}"
    )

# CALCULATE TOTAL DEBIT AND CREDIT
credit_total = sum(
    (balances["credit"] for balances in trial_balance.values()),
    Decimal("0"),
)
debit_total = sum(
    (balances["debit"] for balances in trial_balance.values()),
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

# VALIDATE NORMAL BALANCE MAPPING
missing_accounts = [
    account for account in trial_balance if account not in normal_balance
]
if missing_accounts:
    raise ValueError(
        f"Normal balance not defined for accounts: {', '.join(missing_accounts)}"
    )

for account, balance in normal_balance.items():
    if balance not in ("debit", "credit"):
        raise ValueError(
            f"Invalid normal balance for account '{account}': {balance}. Must be 'debit' or 'credit'."
        )

# ABNORMAL BALANCE ANALYSIS
print("\nABNORMAL BALANCE ANALYSIS")
print("-----------------------")

exception_accounts = []
zero_balance_accounts = []
account_analysis = []

for account, balances in trial_balance.items():
    net_balance = balances["debit"] - balances["credit"]

    if net_balance > 0:
        balance_amount = net_balance
        actual_side = "debit"
    elif net_balance < 0:
        balance_amount = abs(net_balance)
        actual_side = "credit"
    else:
        balance_amount = Decimal("0")
        actual_side = "zero"

    expected_side = normal_balance[account]

    if actual_side == "zero":
        status = "ZERO BALANCE"
        zero_balance_accounts.append(account)
    elif actual_side == expected_side:
        status = "NORMAL"
    else:
        status = "INVESTIGATE"
        exception_accounts.append({
            "account": account,
            "balance_amount": balance_amount,
            "actual_side": actual_side,
            "expected_side": expected_side,
        })

    account_analysis.append({
        "account": account,
        "balance_amount": balance_amount,
        "actual_side": actual_side,
        "expected_side": expected_side,
        "status": status,
    })

    print(
        f"{account:<25}: "
        f"Rp{balance_amount:,.0f}, "
        f"{actual_side.upper():<7}, "
        f"status: {status}"
    )

# EXCEPTION REPORT 

print("\nEXCEPTION REPORT")
print("-----------------------")

if exception_accounts.append:
    for item in exception_accounts:
        print(
            f"Account: {item['account']:25}"
            f"Balance: Rp{item['balance_amount']:,.0f}, "
            f"Actual Side: {item['actual_side'].upper():<7}, "
            f"Expected: {item['expected_side'].upper():<7}"
        )
else:
    print("No abnormal balances found.")
    
