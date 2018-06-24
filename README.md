# Portship

Python-based ROSE Online asset extraction utility - probably the fastest to ever exist.

## Requirements

Your system needs a few utilities in order to run all of the conversions. Below is a
full list of requirements and below it are platform-specific package names for them.

If your platform isn't listed, ensure the following are available and on your PATH.

- a C compiler aliased to `cc` (usually the default)
- [Ninja](https://ninja-build.org)
- [ImageMagick](https://www.imagemagick.org) (specifically `convert`)

#### Ubuntu

```console
$ apt-get install ninja-build build-essential

### Ubuntu11.10+ ###
$ apt-get install python-pgmagick

### Ubuntu10.04+ ###
$ apt-get install libgraphicsmagick++1-dev
$ apt-get install libboost-python1.40-dev
```

#### MacOS

```console
$ brew install ninja graphicsmagick
$ brew install boost-python --with-python3
```

Additionally, you'll need to install Xcode if you don't already have a C compiler.

#### Windows

Windows is not (currently) supported. Feel free to send a PR with instructions/adjustments
to make that possible.

CYGWIN or Msys environments should work fine assuming you have the relevant packages installed.

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

To use Portship, locate the `.IDX` file in your ROSE installation directory (usually called `index.idx` or `data.idx` - there will be only one)
and create a directory where you want the files to be generated.

Once complete, run the following:

```console
$ portship /path/to/data.idx /path/to/destination_dir/
```

That process should only take a few seconds, after which a `build.ninja` file will be generated in the destination directory.

`cd` into the destination directory and run:

```console
$ ninja
```

Ninja will perform all of the steps necessary to extract and convert all of the assets.

### How do I extract all assets without converting?

Some users may not care about the conversions and simply need the raw assets unpacked from the VFS files.

Just run

```console
$ ninja raw_assets
```

# License

Released under the MIT license.
