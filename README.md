# pippity
Install your PyPi packages without access to pip. Install packages, straight from inside your script.

## Installation

To install pippity, just run the following command in a shell with access to python/pip:
```shell
pip install pippity
```

## Documentation
Using pippity to install packages from PyPi is really easy!

```python
import pippity

result = pippity.install("numpy")
# Returns an InstallResult object.

print(result.ok) # Boolean value, whether it installed correctly or not.

print(result.stdout) # pip's stdout

print(result.stderr) # pip's stderr
```

Or, if you want to install multiple packages:

```python
import pippity

result = pippity.install(["flask", "uvicorn"])

print(result.ok)
print(result.stdout)
print(result.stderr)
```

You can use this at the start of a script, for example:

```python

import pippity
import sys

try:
    import package1
    import package2
    import package3
except ImportError:
    print("Packages not detected. Installing now...")
    result = pippity.install(["package1", "package2", "package3"])
    if result.ok:
        print("Packages installed successfully!")
        import package1
        import package2
        import package3
    else:
        print("Packages failed to install. STDERR:")
        print(result.stderr)
        sys.exit(1)
```
