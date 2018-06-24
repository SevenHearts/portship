# Portship

Python-based ROSE Online asset extraction utility - probably the fastest to ever exist.

## Requirements

```console
### Ubuntu11.10+ ###
$ apt-get install python-pgmagick

### Ubuntu10.04+ ###
$ apt-get install libgraphicsmagick++1-dev
$ apt-get install libboost-python1.40-dev
```

MacOS:

```console
$ brew install graphicsmagick
$ brew install boost-python --with-python3
```

Windows is not (currently) supported.

## Installing

_Optionally_, start a virtual environment

```console
$ virtualenv env
$ . env/bin/activate
```

Then install the dependencies

```console
$ python setup.py install
```

## Running

TBD

# License

Released under the MIT license.
