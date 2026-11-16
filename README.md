# Accounting Python Foundations

A practical Python project focused on accounting automation, financial data validation, and audit-oriented controls.

## Project Overview

This repository documents my learning journey in combining accounting knowledge with Python programming to develop practical accounting automation tools.

The objective is to build a foundation in:
- Accounting data processing
- Journal validation
- Automated trial balance preparation
- Abnormal balance detection
- Transaction-level audit and risk detection
- Automated testing and reporting

## Project Structure

```text
accounting-python-foundations/
│
├── journal_check.py
├── abnormal_balance.py
├── README.md
└── (Upcoming modules)
```

## Learning Roadmap

| Mission | Project | Status |
|---|---|---|
| 01 | Journal Validation | Completed |
| 02 | Automated Trial Balance | Completed |
| 03 | Abnormal Balance Detection | Completed |
| 04 | Automated Journal Audit & Risk Detection | In Progress |

## Mission 01 — Journal Validation

Developed a basic journal validation program using Python.

Key features:
- Debit and credit validation
- Negative transaction detection
- Empty journal entry detection
- Journal balance verification
- Decimal-based financial calculations

## Mission 02 — Automated Trial Balance

Developed an automated trial balance calculation system.

Key features:
- Transaction aggregation by account
- Automated debit and credit totals
- Trial balance generation
- Balance difference identification

## Mission 03 — Abnormal Balance Detection

Developed an accounting control system to identify abnormal account balances.

Key features:
- Ending balance calculation
- Normal balance mapping
- Debit and credit side identification
- Account classification:
  - NORMAL
  - INVESTIGATE
  - ZERO BALANCE
- Automated exception reporting
- Automated test assertions
- Separate original and test datasets

### Test Results

| Account | Expected Classification |
|---|---|
| Cash | NORMAL |
| Accounts Receivable | NORMAL |
| Equipment | NORMAL |
| Accounts Payable | INVESTIGATE |
| Capital | NORMAL |
| Rent Expense | ZERO BALANCE |

Trial balance test:
- Total Debit: Rp19,000,000
- Total Credit: Rp14,500,000
- Difference: Rp4,500,000
- Status: NOT BALANCED

Note: Trial balance validation and abnormal balance detection are separate accounting controls.

## Mission 04 — Automated Journal Audit & Risk Detection

Currently in development.

Planned features:
- Duplicate transaction detection
- Unusual transaction identification
- Missing account validation
- Transaction-level exception reporting
- Audit trail and risk classification

## Technology Stack

- Python
- Decimal module
- Git
- GitHub
- Visual Studio Code

## Learning Philosophy

This project emphasizes practical learning through accounting scenarios, structured problem-solving, automated controls, and continuous improvement.

The objective is not merely to write Python code, but to understand how accounting principles can be translated into reliable automated systems.

## Author

Accounting Student | Aspiring Accounting & Finance Professional

**Project:** Accounting Python Foundations