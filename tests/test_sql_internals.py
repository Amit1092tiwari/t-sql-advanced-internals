import os
from pathlib import Path
import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent

def test_repository_governance_files():
    """Verify presence of core open-source governance and licensing assets."""
    required = ["LICENSE", "CONTRIBUTING.md", "SECURITY.md", "readme.md"]
    for f in required:
        file_path = REPO_ROOT / f
        assert file_path.exists(), f"Missing required asset: {f}"
        assert file_path.stat().st_size > 0, f"File cannot be empty: {f}"

def test_sql_puzzle_files_exist():
    """Verify that core puzzle specifications and DDL files are present and populated."""
    sql_files = list(REPO_ROOT.glob("**/*.sql"))
    assert len(sql_files) >= 2, "Expected core puzzle DDL and solution SQL files"
    
    for sql in sql_files:
        content = sql.read_text(encoding="utf-8", errors="ignore").strip()
        assert len(content) > 100, f"SQL file {sql.name} is unexpectedly small"
        assert not content.startswith("ERROR"), f"SQL file {sql.name} contains errors"

def test_query_syntax_determinism():
    """Verify common T-SQL deterministic keywords in solution files."""
    solutions = list(REPO_ROOT.glob("**/Advanced SQL Puzzles Solutions.sql"))
    if not solutions:
        solutions = list(REPO_ROOT.glob("**/*Solutions*.sql"))
    
    assert len(solutions) > 0, "Solutions SQL file must exist"
    content = solutions[0].read_text(encoding="utf-8", errors="ignore").upper()
    
    # Assert usage of advanced enterprise window functions & CTEs
    assert "WITH" in content, "Expected CTE usage in solutions"
    assert "OVER (" in content, "Expected window function usage in solutions"
    assert "PARTITION BY" in content, "Expected partition windowing in solutions"
