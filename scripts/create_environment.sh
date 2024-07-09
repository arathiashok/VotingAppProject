rm .venv -r
python -m venv .venv
. .venv/Scripts/activate

pip install poetry
cd app
poetry install