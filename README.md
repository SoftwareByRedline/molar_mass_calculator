# molar_mass_calculator
A simple text-based molar mass calculator Python script.

--------------------------------------------------------------------------------------------------------------------------------------
## Requirements
`python3` installed (will install automatically with .deb package)
## Install (choose one of two)
### 1. Download Zip:
Click the "download zip" button in GitHub's clone menu.
### 2. Clone Git repository:
Requires `git` installed

Type command `git clone https://github.com/SoftwareByRedline/molar_mass_calculator/` in terminal, from the directory you want it installed into.

## Run


Run command `python3 molar.py` from the directory it's installed. (ex. if it's in your `/xyz` directory, run `python3 /xyz/molar_mass_calculator/molar.py`)

------------------------------------------------------
## Use module
You can use the script `molarm.py` as a module for your Python scripts and notebooks.

### Import module

First, ensure that you have a copy of `molarm.py` in the same directory as your script/notebook.

Then, include

`import molarm`

at the top of your script.

After that, you can use the `molarmass` function anywhere in that script/notebook:

`molarm.molarmass("HCl")`

(the above line returns 36.46)
