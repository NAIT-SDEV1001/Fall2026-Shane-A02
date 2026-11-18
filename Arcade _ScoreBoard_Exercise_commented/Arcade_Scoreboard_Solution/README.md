# Arcade Scoreboard Solution

Requires Python 3.9 or later. Open this project folder in VS Code. In its terminal,
run the command from the folder that contains the `arcade_scoreboard` package.

```bash
python -m arcade_scoreboard
```

Record Sam with 900 points and quit. Open `arcade_scoreboard/data/scores.csv`
to see the saved row. Run the same command again, show the board, then find
Sam's 900-point entry.

- `__main__.py` imports and calls `main()` from `app.py`.
- `app.py` runs the menu and decides when to load and save.
- `score_entry.py` defines how one score displays and compares.
- `scoreboard.py` keeps entries in recording order and finds exact matches.
- `score_files.py` converts CSV rows to score objects and writes the board.

The starter CSV contains just the header. To reset the demo, remove the CSV
while the program is closed. The next run starts with an empty board, and
quitting recreates the file.
