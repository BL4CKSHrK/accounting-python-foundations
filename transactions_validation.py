# TRANSACTIONS ACCUMULATION

from decimal import Decimal
from journal_audit import journal


transaction_summary = {}

for entry in journal: 

    transaction_id = entry.get("transaction_id")

    if not transaction_id:
        continue

    if transaction_id not in transaction_summary:
        transaction_summary[transaction_id] = {
            "debit": Decimal("0"),
            "credit": Decimal("0"),
            "line_count": 0,
        }

    transaction_summary[transaction_id]["debit"] += Decimal(
        str(entry.get("debit",0))
    )

    transaction_summary[transaction_id]["credit"] += Decimal(
        str(entry.get("credit",0))
    )
# DISPLAY TRANSACTION SUMMARY 

print("\nTRANSACTION SUMMARY")
print("---------------------")

for transaction_id, balance in transaction_summary.items():

    print(
        f"{transaction_id}:"
        f"Debit = Rp{balance['debit']:,.0f},"
        f"Credit = Rp{balance['credit']:,.0f},"
        f"Lines = {balance['line_count']}"
    )