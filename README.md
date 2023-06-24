# Tilepaint Puzzle App Repository

Tilepaint (Tairupeinto) is a logic pencil-and-paper puzzle that has proven NP-Complete. The verification and solver related to the Tilepaint puzzles are in this repository. We implemented the solver using Exhausted Search (Brute force) and Prune-and-Search (Backtracking)
with the asymptotic time complexity runnning time $O(2^{p} \cdot mn)$, where $m \times n$ is the size of the instance. For more information about the puzzle, see [https://www.nikoli.co.jp/en/puzzles/tilepaint/](https://www.nikoli.co.jp/en/puzzles/tilepaint/).
## Local Installation

This app uses Django framework and PySAT library. To use this app locally, clone this repository and then run the following command to install the required dependencies using pip:
```
pip install -r requirements.txt
```
Next, run the app with the following command:
```
python manage.py runserver
```
You can then open your browser and visit the app on http://localhost:8000.
