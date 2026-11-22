# 📐 T-SQL Algorithmic Complexity & Execution Plan Guide

This document establishes performance engineering principles for enterprise SQL Server relational queries, window functions, and set-based algorithms.

---

## 1. Sargability Principles (Search Argument Ability)

A query predicate is **sargable** if the relational engine's query optimizer can leverage an index seek rather than scanning the entire index or table.

| Anti-Pattern (Non-Sargable Scan) | Optimized Pattern (Sargable Index Seek) | Complexity Impact |
| :--- | :--- | :--- |
| `WHERE YEAR(TransactionDate) = 2026` | `WHERE TransactionDate >= '2026-01-01' AND TransactionDate < '2027-01-01'` | $O(N) \longrightarrow O(\log N)$ |
| `WHERE ISNULL(Status, 'ACTIVE') = 'ACTIVE'` | `WHERE Status = 'ACTIVE' OR Status IS NULL` | Eliminates table spool |
| `WHERE SUBSTRING(AccountNumber, 1, 3) = '901'` | `WHERE AccountNumber LIKE '901%'` | Leverages b-tree prefix seek |

---

## 2. Window Function Memory Grants & Operators

When executing advanced window functions (`ROW_NUMBER()`, `DENSE_RANK()`, `SUM() OVER (...)`):

1. **Segment & Sequence Project:** If an index exists matching `PARTITION BY <cols> ORDER BY <cols>`, SQL Server reads pre-sorted streams in $O(N)$ with near-zero memory grant.
2. **Sort Spool Warning:** If no matching index exists, SQL Server injects an eager `Sort` operator ($O(N \log N)$), requiring an explicit memory grant that can spill to `tempdb` under concurrency.

---

## 3. Recursive CTE Termination Heuristics

All recursive Common Table Expressions (hierarchies, bill-of-materials, graph traversals) must enforce:
* Deterministic termination predicate on level/depth: `WHERE Depth < 100`.
* The `MAXRECURSION` query hint (`OPTION (MAXRECURSION 100)`) to protect relational buffer pools from infinite looping.
