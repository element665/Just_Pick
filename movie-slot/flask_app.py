import random
from flask import Flask, render_template, request, redirect, url_for

FILE_PATH = "./movie_list.txt"
SLOT_COUNT = 3

app = Flask(__name__)

# ---------- Data ----------

def load_movies(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]

movies = load_movies(FILE_PATH)
used_movies = set()

slots = [""] * SLOT_COUNT
locked = [False] * SLOT_COUNT


# ---------- Slot Logic ----------

def spin_slot(available, used):
    choices = [m for m in available if m not in used]
    return random.choice(choices) if choices else None


def spin_slots():
    global slots, locked, used_movies

    for i in range(SLOT_COUNT):
        if locked[i]:
            continue

        final = spin_slot(movies, used_movies)
        if final:
            used_movies.add(final)
            slots[i] = final


# ---------- Routes ----------

@app.route("/", methods=["GET", "POST"])
def index():
    global locked

    if request.method == "POST":
        action = request.form.get("action")

        if action == "spin":
            spin_slots()

        elif action == "clear":
            locked = [False] * SLOT_COUNT

        elif action.startswith("toggle"):
            idx = int(action[-1])
            locked[idx] = not locked[idx]

        return redirect(url_for("index"))

    return render_template(
        "index.html",
        slots=slots,
        locked=locked
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
