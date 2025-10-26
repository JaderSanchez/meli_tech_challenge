# Mercado Libre Technical Challenge

Solutions to the Mercado Libre technical challenge. Each problem is solved in a separate directory with detailed documentation.

## Prerequisites

- **Python 3.x**
- **Go 1.25.3+**
- **MySQL or PostgreSQL** (for SQL problem)

## Setup and Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd meli_tech_challenge
```

### 2. Install Python dependencies

```bash
cd 2_best_in_genre
pip install -r requirements.txt
cd ..
```

### 3. Install Go dependencies

```bash
cd 4_summarizer
go mod download
cd ..
```

## Running the Solutions

### Problem 1: Minesweeper (Python)

```bash
cd 1_minesweeper
python solution_minesweeper.py
```

### Problem 2: Best in Genre (Python)

```bash
cd 2_best_in_genre
python solution_best_in_genre.py
```

### Problem 3: Advertising System Failures Report (SQL)

```bash
cd 3_advertising_system_failures_report
psql -d your_database -f setup.sql
psql -d your_database -f solution_advertising_system_failures_report.sql
```

### Problem 4: Summarizer (Go)

```bash
cd 4_summarizer

# Short summary (1-2 sentences)
go run solution_summarizer.go -t short texts_samples/aws_fail_october_2025.txt

# Medium summary (paragraph)
go run solution_summarizer.go -t medium --input texts_samples/aws_fail_october_2025.txt

# Bullet points summary
go run solution_summarizer.go --type bullet --input texts_samples/aws_fail_october_2025.txt
```

## Project Structure

```
meli/
├── 1_minesweeper/
│   ├── problem.md
│   └── solution_minesweeper.py
├── 2_best_in_genre/
│   ├── problem.md
│   ├── requirements.txt
│   └── solution_best_in_genre.py
├── 3_advertising_system_failures_report/
│   ├── problem.md
│   ├── setup.sql
│   └── solution_advertising_system_failures_report.sql
└── 4_summarizer/
    ├── problem.md
    ├── go.mod
    ├── solution_summarizer.go
    ├── texts_samples/
    └── summarizes_samples/
```

## Notes

Each problem directory contains a `problem.md` file with detailed requirements and approach documentation.
