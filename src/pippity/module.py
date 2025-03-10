import sys
import subprocess
from typing import List, Union

class InstallResult():
    def __init__(self, ok, stdout, stderr):
        self.ok = ok
        self.stdout = stdout
        self.stderr = stderr

def install(packages: Union[str, List[str]]) -> InstallResult:
    """
    Installs one or more Python packages using pip.

    Args:
        packages (str or list of str): The name of a single package or a list of package names to install.


    Returns:
        InstallResult: An object containing the result of the installation.
    
    """

    if isinstance(packages, str):
        packages_to_install = [packages]
    elif isinstance(packages, list):
        packages_to_install = packages
    else:
        raise TypeError("Packages must be a string or a list of strings.")


    if not sys.executable:
        return InstallResult(False, "", "Python Executable not found.")

    cmd = [sys.executable, "-m", "pip", "install"]
    cmd.extend(packages_to_install)
    
    try:
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        return InstallResult(True, result.stdout.decode(), result.stderr.decode())
    
    except subprocess.CalledProcessError as e:
        return InstallResult(False, "", e.stderr.decode())

    except Exception as e:
        return InstallResult(False, "", str(e))
