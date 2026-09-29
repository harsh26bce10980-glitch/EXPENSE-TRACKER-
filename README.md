# Expense Tracker (Python Console Application)

A command-line application for recording, analyzing, and monitoring personal
expenses. Records are stored locally in a plain text file so data persists
between runs.

**Submitted by:** Harsh Godara (Reg. No. 26BCE10980)
**Course:** B.Tech – CSE CORE
**Submitted to:** Dr. AVR Mayuri

---

## Features

- Add an expense (name, amount, category)
- View all recorded expenses
- Calculate total spending
- View category-wise spending breakdown
- Identify the highest individual expense
- Set a monthly budget and view remaining budget
- Local file persistence (`expense.txt`)
- Input validation with exception handling (invalid numbers, empty fields,
  zero/negative amounts)

## Requirements

- Python 3.7+
- No external dependencies (standard library only)

## How to Run

```bash
python expense_tracker.py
```

You'll see a menu:

```
========== EXPENSE TRACKER ==========
1. Add Expense
2. View All Expenses
3. View Total Spending
4. View Category-wise Spending
5. View Highest Expense
6. Set Monthly Budget
7. View Budget Status
8. Exit
======================================
```

Enter the number corresponding to the action you want to perform.

## Data Storage Design

Expenses are stored in `expense.txt`, one record per line, with fields
separated by `|`:

```
name|amount|category
```

| Field         | Example        | Purpose                     |
|---------------|----------------|------------------------------|
| Expense Name  | College Canteen| Identifies the expense       |
| Amount        | 120.0          | Stores the monetary value    |
| Category      | FOOD           | Groups related expenses      |

The file is created automatically the first time an expense is added, and
is re-loaded automatically each time the program starts.

## Project Structure

```
expense_tracker.py   # Main application
expense.txt          # Auto-generated data file (created on first run)
README.md            # This file
```

## Implementation Notes

- Expenses are held in memory as a list of dictionaries during the session.
- A dictionary is used to aggregate category-wise totals dynamically (no
  hard-coded category list).
- `try/except` blocks guard all numeric input and file I/O so the program
  never crashes on bad input.
- The monthly budget is **session-only** and is not written to disk — this
  matches the scope described in the project report.

## Known Limitations

- Command-line only; no GUI.
- Monthly budget resets each time the program restarts.
- Text-file storage is best suited to small datasets (no indexing/search).
- No authentication or multi-user support.

## Possible Future Enhancements

- Add date/month tracking to each expense
- Search and filter expenses
- Generate monthly summary reports
- Export records to CSV
- Visualize spending with charts
- Move from text-file storage to a proper database
- Persist the monthly budget across sessions

## Sample Test Data

The following data set (used for testing/screenshots in the project report)
can be used to verify the program works as expected:

| Name            | Amount | Category      |
|-----------------|--------|---------------|
| College Canteen | 120    | FOOD          |
| Bus Pass        | 200    | TRAVEL        |
| Notebook        | 180    | EDUCATION     |
| Movie           | 250    | ENTERTAINMENT |
| Lunch           | 150    | FOOD          |

Expected results with this data:
- **Total spending:** ₹900
- **Category totals:** FOOD 270, TRAVEL 200, EDUCATION 180, ENTERTAINMENT 250
- **Highest expense:** Movie, ₹250
- **Budget status:** with a ₹2000 budget set, ₹1100 remains
