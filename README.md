# Brisbane
A very simple clustering script for bike stations 


## Project's structure
This project structure is based on [The hitchhiker's Guide to Python](https://docs.python-guide.org/writing/structure/).

## Python version and virtualenv
This project runs with Python 3.6.7 and was used along [pyenv](https://github.com/pyenv/pyenv) and its plugin
[pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)

Once the two are installed, you can simply run the following in the project's root:
```
make init
```

## Usage
Make sure you put the file `Brisbane_CityBike.json` in a `data` folder at the root of the project.


Then run:
> python . -f data/Brisbane_CityBike.json -p -c position -n 2

And you will obtain the resulted two clusters in the default output file `data/clusters_result.json`

For all available options, type:
> python . --help