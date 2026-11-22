# Enterprise SQL & Cloud Data Engineering Masterclass (`t-sql-advanced-internals`)

[![SQL Engine CI](https://github.com/Amit1092tiwari/t-sql-advanced-internals/actions/workflows/sql-ci.yml/badge.svg)](https://github.com/Amit1092tiwari/t-sql-advanced-internals/actions/workflows/sql-ci.yml)
[![Daily Batch Job](https://github.com/Amit1092tiwari/t-sql-advanced-internals/actions/workflows/daily-batch.yml/badge.svg)](https://github.com/Amit1092tiwari/t-sql-advanced-internals/actions/workflows/daily-batch.yml)
[![Pages Deployment](https://github.com/Amit1092tiwari/t-sql-advanced-internals/actions/workflows/static.yml/badge.svg)](https://github.com/Amit1092tiwari/t-sql-advanced-internals/actions/workflows/static.yml)
[![Platform](https://img.shields.io/badge/Platform-MSSQL%20%7C%20PostgreSQL%20%7C%20Snowflake%20%7C%20BigQuery%20%7C%20DuckDB-blue.svg)](#cross-engine-capability-matrix)
[![Cloud](https://img.shields.io/badge/Azure-Data%20Factory%20%7C%20Databricks%20%7C%20Delta%20Lake%20%7C%20Terraform-orange.svg)](#-microsoft-azure-cloud-data-engineering--iac)
[![Puzzles](https://img.shields.io/badge/Puzzles-55%20Core%20%2B%2011%20Bonus-brightgreen.svg)](#-55-advanced-sql-puzzles-directory)

A production-grade relational database and cloud data engineering benchmark platform. This repository bridges theoretical set-based relational problem-solving with enterprise data engineering patterns across **Microsoft SQL Server (T-SQL)**, **PostgreSQL 16+**, **Snowflake**, **Google BigQuery**, **DuckDB**, and **Microsoft Azure**.

---

## 🌟 Why This Repository Exists: The Enterprise Evolution

Most online SQL puzzle resources exist as isolated snippets or static PDFs focused solely on single-engine syntax. This repository elevates the classic puzzle corpus into a **modern, polyglot software engineering benchmark**:

1. **Zero Binary Bloat (100% Markdown):** All legacy PDF and PPTX files have been excised and transcribed into version-controlled Markdown with KaTeX math, Mermaid query lifecycles, and Three-Valued Logic (3VL) truth tables.
2. **Multi-Dialect Polyglot Architectures:** Concrete, runnable solutions demonstrating how the same relational problem is tackled using modern cloud primitives—such as Snowflake's `MATCH_RECOGNIZE`, BigQuery's `QUALIFY` and `COUNTIF()`, and PostgreSQL's `FILTER (WHERE ...)` and array operators.
3. **Automated Dockerized CI Pipeline:** Every commit boots an ephemeral **Microsoft SQL Server 2022** Linux container to compile and validate all DDL, stored procedures, and functions.
4. **Security & Performance Hardening:** Production-grade security optimizations (e.g. `QUOTENAME()` escaping and aggregate whitelisting in dynamic PIVOT stored procedures) and zero-overhead inline table-valued functions (iTVFs).
5. **Production Cloud Data Engineering & IaC:** Real-world Azure Data Factory metadata ingestion pipelines, Databricks Spark and Delta Lake architectures, accompanied by **Terraform and Azure Bicep Infrastructure-as-Code (IaC)**.

---

## 🌐 Interactive Web Portal

Browse and search all 55 puzzles, utilities, and whitepapers via the live GitHub Pages portal:  
👉 **[Launch Enterprise SQL Web Directory](https://amit1092tiwari.github.io/Advancesqlpuzzle/)**

---

## ⚡ Cross-Engine Capability Matrix

| Architectural Pattern | Microsoft SQL Server (T-SQL) | PostgreSQL (16+) | Snowflake | Google BigQuery | DuckDB |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Window Filtering (`QUALIFY`)** | ❌ (CTE Wrapping) | ❌ (CTE Wrapping) | ✅ Native Storage Pushdown | ✅ Native Storage Pushdown | ✅ Native In-Memory |
| **Row Pattern (`MATCH_RECOGNIZE`)** | ❌ | ❌ | ✅ Native $O(N)$ Streaming | ❌ | ❌ (Double ROW_NUMBER) |
| **Recursive Syntax** | `WITH cte AS (...)` | `WITH RECURSIVE` | `WITH RECURSIVE` / `CONNECT BY` | `WITH RECURSIVE` | `WITH RECURSIVE` |
| **Conditional Aggregation** | `SUM(CASE WHEN ...)` | `SUM(...) FILTER (WHERE ...)` | `COUNT_IF(...)` / `IFF()` | `COUNTIF(...)` | `SUM(...) FILTER (WHERE ...)` |
| **Native Array Types** | ❌ (JSON Strings) | ✅ Native Array (`=`, `&&`) | ✅ Native Array / Variant | ✅ Native Array / Struct | ✅ Native List / Struct |
| **Set Difference** | `EXCEPT` | `EXCEPT` | `EXCEPT` / `MINUS` | `EXCEPT DISTINCT` | `EXCEPT` |

---

## 📂 Repository Architecture

```text
t-sql-advanced-internals/
├── .github/
│   └── workflows/
│       ├── daily-batch.yml                     # Scheduled daily regression & polyglot benchmark batch job
│       ├── sql-ci.yml                          # Ephemeral MSSQL 2022 container CI testing
│       └── static.yml                          # GitHub Pages automated deployment pipeline
├── Advanced SQL Puzzles/
│   ├── ADVANCED_SQL_PUZZLES.md                 # Complete specs for 55 puzzles + 11 bonus puzzles
│   ├── Advanced SQL Puzzles DDL.sql            # Schemas & sample data for Puzzles #1 - #55
│   ├── Advanced SQL Puzzles Solutions.sql      # Multi-strategy T-SQL solutions
│   └── readme.md
├── Database Tips and Tricks/
│   ├── Calendar Table/                         # High-performance calendar dimension ITVF & daily rolling proc
│   ├── Data Profiling/                         # Table metadata, statistical distributions, & quality profiler
│   ├── Pivoting Data/                          # SQL-injection safe dynamic PIVOT stored procedure
│   ├── Subtracting Two Dates/                  # Nanosecond-precision interval difference routines
│   └── readme.md
├── Database Writings/
│   ├── Advanced SQL Joins/                     # Mechanics of SQL joins, 3VL, & physical operators
│   ├── Behavior Of Nulls/                      # Three-valued logic whitepaper & truth tables
│   ├── Database Concepts And Components/       # 129 core engine, storage, and indexing Q&As
│   └── readme.md
├── Microsoft Azure/
│   ├── Infrastructure as Code/                 # One-click Terraform (main.tf) & Azure Bicep
│   ├── Data Factory Metadata Demo/             # ADF metadata auditing, TVP pipeline & DailyScheduleTrigger.json
│   ├── Databricks Spark Hive Demo/             # Spark SQL, Hive metastore, & Delta Lake integration
│   └── readme.md
├── Multi-Dialect Solutions/
│   ├── MULTI_DIALECT_GUIDE.md                  # Paradigm guide: Gaps & Islands, QUALIFY, Recursion
│   ├── PostgreSQL_Solutions.sql                # PostgreSQL 16+ solutions (FILTER, Arrays, CTEs)
│   ├── Snowflake_Solutions.sql                 # Snowflake solutions (MATCH_RECOGNIZE, QUALIFY)
│   ├── BigQuery_Solutions.sql                  # Google BigQuery solutions (COUNTIF, STRUCTs)
│   ├── DuckDB_Solutions.sql                    # Fast in-memory analytical SQL solutions
│   └── readme.md
├── scripts/
│   └── daily_benchmark.py                      # Multi-dialect DuckDB benchmark & assertion engine
├── .gitattributes                              # Clean EOL normalization & binary rules
├── .nojekyll                                   # Bypasses Jekyll on GitHub Pages
├── index.html                                  # Modern, client-side searchable web portal
└── readme.md                                   # Masterclass architectural documentation
```

---

## 🧩 55 Advanced SQL Puzzles Directory

The puzzles test deep problem-solving skills across complex relational algorithms:

| Category | Puzzle Numbers & Topics |
| :--- | :--- |
| **Hierarchies & Recursion** | **#2** Managers & Employees (Hierarchical Trees), **#11** Permutations, **#41** Associate IDs |
| **Gaps & Islands** | **#6** Workflow Steps, **#28** Fill the Gaps (LOCF), **#29** Count Groupings, **#47** Work Schedule |
| **Pivoting & Unpivoting** | **#5** Phone Directory, **#17** De-grouping, **#52** Phone Numbers Unpivot |
| **Relational Division & Sets** | **#1** Shopping Carts, **#7** Mission to Mars, **#9** Matching Sets, **#21** Table Differences, **#54** Winning Numbers, **#55** Table Audit (Single-pass FULL OUTER JOIN) |
| **Window Functions & Ranking** | **#4** Two Predicates, **#12** Average Days, **#24** Page Views, **#25** Top Vendors, **#26** Previous Year Sales, **#31** Second Highest, **#43** Unbounded Preceding, **#48** Consecutive Sales |
| **Temporal & SCD Modeling** | **#19** Back to the Future, **#44** Slowly Changing Dimension (SCD Type 2) Part I, **#45** SCD Part II |
| **Mathematics & Statistics** | **#10** Mean, Median, Mode & Range, **#36** Traveling Salesman, **#39** Prime Numbers Sieve, **#49** Sum of Hex Values |
| **Data Integrity & Logic** | **#3** Fiscal Year Table Constraints, **#8** Workflow Cases, **#13** Inventory Tracking, **#14** Indeterminate Logs, **#16** Reciprocals, **#18** Seating Chart, **#20** Price Points, **#27** Delete Duplicates, **#30** Select Star, **#32** First & Last, **#33** Deadlines, **#34** Specific Exclusion, **#35** Domestic vs International, **#37** Group Criteria, **#38** Reporting Elements, **#40** Sort Order, **#42** Mutual Friends, **#46** Positive Balances, **#50** Terms Clarification, **#51** Primary & Secondary Keys, **#53** Spouse Pairings |

---

## 🛠️ Enterprise Database Utilities (`Database Tips and Tricks`)

### 1. Deterministic Calendar Dimension Table (`FnReturnCalendarTable.sql`)
- Zero-overhead inline table-valued function generating full calendar attributes.
- Native string parsing (eliminates costly .NET CLR `FORMAT()` context switches).
- Full Gregorian leap year century calculation rule support.
- Weekday calculation independent of session-level `@@DATEFIRST` configuration.

### 2. SQL-Injection Hardened Dynamic PIVOT (`SpPivotData.sql`)
- Secure dynamic pivoting stored procedure utilizing `QUOTENAME()` on all identifiers.
- Strict input whitelisting for aggregate functions (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`).
- Automated XML entity decoding and clean column alias construction.

### 3. High-Precision Date Difference Engine (`FnDateDiffPartsTable.sql` & `FnDateDiffPartsChar.sql`)
- Precision down to the nanosecond (`DATETIME2(7)`).
- Refactored as an **Inline Table-Valued Function (ITVF)**, enabling query optimizer inlining, sub-query unrolling, and full engine parallelism.

### 4. Table Profiler & Metadata Analyzer (`Data Profiling.sql`)
- Comprehensive profiling script computing null percentages, zeros/blanks, distinct values, text length distributions, whitespace/newline flags, and numeric statistics (mean, stdev, sum).

---

## ☁️ Microsoft Azure Cloud Data Engineering & IaC

### 1. One-Click Cloud Infrastructure (Terraform & Bicep)
- Automated deployment scripts in [`Microsoft Azure/Infrastructure as Code/`](file:///c:/Users/amitt/Documents/github/Advancesqlpuzzle/Microsoft%20Azure/Infrastructure%20as%20Code/).
- Provisions: Azure Resource Group, Azure Data Lake Storage Gen2 (`raw`, `curated`, `metadata`), Azure SQL Database, Azure Data Factory (v2) with managed identities, and Azure Databricks.

```bash
cd "Microsoft Azure/Infrastructure as Code"
terraform init && terraform apply
```

### 2. Azure Data Factory Metadata Ingestion Pattern
- Automated metadata harvesting (file size, MD5 hash, column counts, pipeline run IDs).
- Stored procedure ingestion via Table-Valued Parameters (TVP) for high-throughput batching.
- Right-sized enterprise schema data types (`BIGINT` for file sizes, `UNIQUEIDENTIFIER` for run GUIDs, `CHAR(32)` for MD5 hashes).

### 3. Databricks Spark & Hive Metastore Integration
- Classic Suppliers-Parts-Shipments relational design.
- Includes Databricks notebook workspace (`SuppliersAndParts.dbc`) and source SQL Server DDL (`SuppliersAndPartsDDL.sql`).

---

## 🚀 Getting Started

### Prerequisites
- **Database Engine:** Microsoft SQL Server 2016+, PostgreSQL 16+, Snowflake, Google BigQuery, or DuckDB.
- **Client Tools:** SQL Server Management Studio (SSMS), Azure Data Studio, DBeaver, or VS Code.

### Running Puzzles Locally (SQL Server)
1. Clone the repository:
   ```bash
   git clone https://github.com/Amit1092tiwari/t-sql-advanced-internals.git
   cd t-sql-advanced-internals
   ```
2. Open `Advanced SQL Puzzles/Advanced SQL Puzzles DDL.sql` and execute the script to provision sample tables and data.
3. Open `Advanced SQL Puzzles/Advanced SQL Puzzles Solutions.sql` to inspect and execute solutions.

---

## 🤖 Continuous Integration & Verification

The repository includes a GitHub Actions CI pipeline ([`.github/workflows/sql-ci.yml`](file:///c:/Users/amitt/Documents/github/Advancesqlpuzzle/.github/workflows/sql-ci.yml)) that spins up an ephemeral **Microsoft SQL Server 2022** Linux container (`mcr.microsoft.com/mssql/server:2022-latest`) on every push to validate:
- DDL compilation and syntax correctness.
- Utility function and stored procedure creation (`CREATE OR ALTER`).
- Integrity of all SQL puzzle schemas and seed data.

---

## 📄 License & Attribution

- **Original Concept & Problem Statements:** Authored by **Scott Peters** ([advancedsqlpuzzles.com](https://advancedsqlpuzzles.com)).
- **Enterprise Engineering, Polyglot Translations, CI/CD, & Cloud Architectures:** Refactored, expanded, and maintained by **Amitkumar Tiwari** ([GitHub Profile](https://github.com/Amit1092tiwari)).
