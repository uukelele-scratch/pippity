import sys
import subprocess
from typing import List, Optional

class InvalidArgumentsError(TypeError):
    pass

class InstallResult():
    def __init__(self, ok, stdout, stderr):
        self.ok = ok
        self.stdout = stdout
        self.stderr = stderr

def install(package: Optional[str] = None, packages: Optional[List[str]] = None) -> InstallResult:
    """
    Installs one or more Python packages using pip.

    Args:
        package (str, optional): The name of a single package to install.
        packages (list, optional): A list of package names to install.

    Returns:
        InstallResult: An object containing the result of the installation.

    Raises:
        InvalidArgumentsError: If invalid arguments are provided.
    """
    
    if package and packages:
        raise InvalidArgumentsError("Cannot provide package[s] in both list and string form.")

    if package:
        packages_to_install = [package]
    elif packages:
        packages_to_install = packages
    else:
        raise InvalidArgumentsError("Must provide package[s] in either list or string form.")

    if not sys.executable:
        return InstallResult(False, "", "Python Executable not found.")
    
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install"] + packages_to_install,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        return InstallResult(True, result.stdout.decode(), result.stderr.decode())
    
    except subprocess.CalledProcessError as e:
        return InstallResult(False, "", e.stderr.decode())

    except Exception as e:
        return InstallResult(False, "", str(e))