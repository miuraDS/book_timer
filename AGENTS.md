# Repository Guidelines

The `reading_books_timer` app is a Tkinter-based timer for reading sessions. This guide explains structure, workflows, and collaboration expectations.

## Project Structure & Module Organization
- `book_timer` at the repository root is the entry point and currently stores both UI wiring and calculation helpers. Keep pure time/page logic near the top and the Tkinter widget assembly grouped together near the bottom for clarity.
- When new modules are needed, add Python files under a `modules/` directory in the root and import them into `book_timer`. Store future icons, fonts, or CSV assets in `assets/` (create it if absent) and reference them with relative paths.

## Build, Test, and Development Commands
- `python -m venv .venv` then `.venv\Scripts\activate` sets up an isolated environment; Tkinter ships with CPython on Windows.
- `python book_timer` launches the GUI locally. Use `python -m idlelib.pyshell book_timer` when you need an interactive console alongside the window.
- `python -m pip install --upgrade pip tk` refreshes the bundled Tkinter and keeps the environment ready for contributors.

## Coding Style & Naming Conventions
- Follow PEP 8: 4-space indentation, snake_case for functions and variables, and PascalCase for any classes. Keep user-facing strings grouped and reuse them instead of duplicating literals.
- Prefer small, testable helpers for calculations; document tricky sections with concise comments, and use UTF-8 encoding for mixed Japanese and English text.

## Testing Guidelines
- Manual verification is still primary: run `python book_timer`, step through start/end time scenarios, and confirm computed page totals.
- For automated coverage, add `pytest` cases under `tests/`, naming files `test_*.py`. Organize calculation utilities so they can be imported without starting the GUI.

## Commit & Pull Request Guidelines
- Adopt Conventional Commits such as `feat: add break reminder dialog` or `fix: correct page delta rounding` to keep history searchable.
- Keep pull requests focused, describe user-visible changes, link any related tasks, and attach before/after screenshots of the main window when visuals change. Request review before merging.

## Security & Configuration Tips
- Keep personal log files out of version control by listing them in `.gitignore`. Never commit credentials or API keys.
- Validate any planned persistence features (e.g., CSV export) to avoid writing malformed data or leaking private information.
