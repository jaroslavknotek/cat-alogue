Cat-alogue
===

Example project showing full-text fuzzy-search across database of cats.
Selected cat can be edited within a detail page.

# Preparation


## Get the code

Option 1: use `git`
```
cd <location>
git clone https://github.com/jaroslavknotek/cat-alogue.git
cv cat-alogue
```

Option 2: download [this archive](https://github.com/jaroslavknotek/cat-alogue/archive/refs/heads/master.zip) and extract it to `<location>`.


In both cases, you should have the code unpacked in the `<location>` folder.


## Install Dependencies

```
cd <location>
python -m venv .venv
# LINUX
. .venv/bin/activate 
# Windows
Scripts/activate.bat

python -m pip install -r requirements.txt
```

# Execute Application

```
python -m streamlit run ui.py
```







