from decimal import Decimal

# Sample accounting transactions
journal = [
    {
        "account": "Cash",
        "debit": Decimal("1500000"),
        "credit": Decimal("0")
    },
    {
        "account": "Service Revenue",
        "debit": Decimal("0"),
        "credit": Decimal("1500000")
    }
]

# Calculate total debit and credit
total_debit = sum(
    (entry["debit"] for entry in journal),
    Decimal("0")
)

total_credit = sum(
    (entry["credit"] for entry in journal),
    Decimal("0")
)

# Validate transactions
for entry in journal:
    if entry["debit"] < 0 or entry["credit"] < 0:
        raise ValueError("Negative transaction detected")

    if entry["debit"] > 0 and entry["credit"] > 0:
        raise ValueError("Invalid journal entry")

    if entry["debit"] == 0 and entry["credit"] == 0:
        raise ValueError("Empty journal entry")

# Display results
print("ACCOUNTING JOURNAL CHECK")
print("------------------------")
print(f"Total Debit : Rp{total_debit:,.0f}")
print(f"Total Credit: Rp{total_credit:,.0f}")

if total_debit == total_credit:
    print("Result: BALANCED")
else:
    print("Result: NOT BALANCED")