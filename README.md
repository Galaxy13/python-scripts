# Galaxy13 Python Scripts Hub

Repository with **Python** scripts, examples and test stuff.

# 1. CVS value comparing script

***CVSCompare_Script.py*** is required to compare 2-column CVS files by their values, using dictionaries.

This script uses **csv** and **optparse** external libraries.

## Install:

First, you need to install external libraries:

```bash
pip install cvs
pip install optparse
```

After that, download this script directly via CLI:

```bash
wget clone https://github.com/Galaxy13/python-scripts.git
```

or just get the script from GitHub.

## Usage

**optparse** library used to determine and parse paths of your CVS files to th script

To launch your script, execute:

```bash
python -m CVSCompare_Script --file1 filepath1 --file2 filepath2
or
python -m CVSCompare_Script --f1 filepath1 --f2 filepath2
```

where **filepath1** and **filepath2** are your paths to files, you are comparing.

Your CVS file should have this structure:

```text
name1, val1
name2, val2
name3, val3
```

and values should **INT** or **FLOAT** type

You can use **tags** or **meanings** of the columns in CVS file, this would be ignored.

# Main contributors:

- **Galaxy13**
