# How to Build tssconfig
As a bare minimum, python3 is required. I use VSCode as a text editor, so the
repository includes a .vscode directory with the required files for this
project. 
Building instructions are OS dependent.

## VSCode
[!NOTE]
You do not need to use VSCode if you prefer other editors. I use it, so I have
included the .vscode directory in the repository. If you use a different editor
for which there are equivalent files, I will be happy to include them.

To install VSCode, follow the instructions on the [VSCode Download page](
    https://code.visualstudio.com/download?_exp_download=fb315fc982).
VSCode is available as a Snap package directly on the download page, and as
a Flatpak on FlatHub. I recommend not using the Flatpak package as I had
problems with using python with it. I did not try the Snap package. If you have
success with either the VSCode Flatpak or the Snap package, please let me know.

Once VSCode is installed, you need the Python extension from Microsoft. This
is available directly from the Visual Studio Marketplace. You can access that
directly from the VSCode Extensions tab.

## Linux
The following instructions assume you are building on a Debian-based distro.
Since __python3__ is included by Linux installs, it is not necessary to install
it. However, you do need __pip__. Since __pip__ is included automatically in
virtual environments and this project has a virtual environment included, you
should be fine.

For the other tools:

```bash
sudo apt install build-essential git
```

And to download and build __tssconfig__, enter:

```bash
cd <your-projects-folder>
git clone https://github.com/jimorc/tssconfig.git
cd tssconfig
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# if using vscode:
code .
# or to build from the command line:
python3 -m src.main # for debug mode, or
python3 -OO -m src.main # for the release version
# to run tests:
python3 -m unittest tests/*test*
```

### Unit Tests
You can run unit tests using the Test Explorer in VSCode, or from the
command line using:
```bash
python3 -m unittest tests/*test*
```
At this time, no tests have been included for UI-related code. 

#### Measuring Test Coverage
Test coverage can be measured in VSCode by selecting the 
__Run Tests With Coverage__
button in the Test Explorer. This generates a test coverage report in the Test
Explorer that lists all directories and python source files. Note that the
test coverage for UI-related files may be 0% since no tests have been
provided for this.
```bash
python3 -m coverage run -m unittest tests/*test*
python3 -m coverage report
```
The report lists only the files, including __init__.py files, that are
referenced by the tests in the test files.