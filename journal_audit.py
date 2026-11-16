from decimal import Decimal

# TRANSACTION DATA STRUCTURE

journal = [
    {
        "transaction_id": "TRX001",
        "date": "2026-11-01",
        "account": "Cash",
        "debit": Decimal("5000000"),
        "credit": Decimal("0"),
    },
    {
        "transaction_id": "TRX002",
        "date": "2026-11-01",
        "account": "Service Revenue",
        "debit": Decimal("0"),
        "credit": Decimal("5000000"),
    },
    {
        "transaction_id": "TRX003",
        "date": "2026-11-03",
        "account": "Expense",
        "debit": Decimal("2000000"),
        "credit": Decimal("0"),
    },
    {
        "transaction_id": "TRTX003",
        "date": "2026-11-03",
        "account": "Cash",
        "debit": Decimal("2000000"),
        "credit": Decimal("0"),
    },
]

# DISPLAY TRANSACTION DATA

print("AUTOMATED JOURNAL AUDIT")
print("------------------------")

for entry in journal:
    print(
        f"ID: {entry['transaction_id']}, |"
        f"Date: {entry['date']}, |"
        f"Account: {entry['account']}, |"
        f"Debit: {entry['debit']:,.0f}, |"
        f"Credit: {entry['credit']:,.0f}, |"
    )
print("------------------------")
print("TOTAL TRANSACTION:", len(journal))
