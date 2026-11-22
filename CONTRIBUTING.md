# Contributing Guidelines

Thank you for your interest in contributing to this repository of enterprise SQL algorithms and execution plan optimizations.

## Standards for Solutions

1. **Deterministic Results**: All queries and puzzle solutions must produce deterministic outputs across SQL Server and target relational engines.
2. **Sargability & Index Awareness**: Queries must avoid non-sargable predicate functions on indexed columns whenever possible.
3. **Execution Plan Documentation**: Complex window functions and recursive queries should include a brief comment explaining the execution strategy or cost characteristics.
4. **Formatting**: Maintain clean SQL indentation with uppercase keywords (`SELECT`, `FROM`, `WHERE`, `JOIN`, `PARTITION BY`).

## Submitting Pull Requests

1. Fork the repository and create your branch from `main`.
2. Ensure queries pass syntax validation.
3. Submit a pull request with a descriptive title explaining the algorithmic challenge or optimization addressed.
