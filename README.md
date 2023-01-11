# SkyrimBG-item-maker
(WIP) Simple python script to automate item cards creation for Skyrim BG (2022)

## Installation

1. Clone this repository.
2. Download `Adobe Garamond Pro Bold.ttf` font from
https://fontsgeek.com/fonts/Adobe-Garamond-Pro-Bold
and place it into cloned repository folder (`./`).
3. Install pgmagick from instructions at:
https://github.com/hhatto/pgmagick
This will require installing pgmagick library (windows executable at: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pgmagick) and install with:
`pip install file.whl`
and boost.python from https://www.boost.org/users/history/version_1_65_0.html
This also requires adding installation path to windows environmental variable PATH.
4. Install requirements with:
`pip install -r requirements.txt`
5. Place xlsx files in `./input` folder (or use sample ones that are placed there already)
6. From main folder (`./`) run:
`python main.py -f filename`
where filename is the name of the input file without extension. Example:
`python main.py -f Potions`
This will generate output files in `./output` folder.
