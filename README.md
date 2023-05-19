Cat-alogue
===

Example project showing full-text fuzzy-search across database of cats.
Selected cat can be edited within a detail page.

# Preparation

Install python. The project was tested with python 3.10.9

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

# Application

Start application with:
```
python -m streamlit run ui.py
```

You will see home page with a list of cats with their picture, name, sex and
age. You can use search bar to find top-5 matches with your query. 

A detail of a cat can be shown by clicking on a cat picture. This will open
another page with a form, where you can edit and save cat information.


