# tssconfig
## About

__tssconfig__ is a program (well, it will be eventually) that processes input files including JPEGs containing the images that should be used in a slide show, as well as a file that contains information about the JPEGs. The output from this program may be used as input to [Flexishow](https://sourceforge.net/projects/flexishow/), or to __tsslideshow__, a program that I plan to create after __tssconfig__.

__tssconfig__ allows the user to:

* select the slides to be displayed.
* sort the slides according to information in the information file.
* generate title slides based on information in the information file.
* create a new information file containing the title slides and images. This file would be input to a second program to control the order in which the slides are displayed.

__tssconfig__ is based on the design of __trilliumshowfx__.



__trilliumshowfx__ was initially designed for a specific purpose: to automate a number of manual processes that are required to take the output from the WordPress Entry Wizard plugin, generate title slides, sort the images, and create a .XLS file for input to __flexishow__.

XLS files suffer from at least two problems:

* XLS files are proprietary to Microsoft Excel. This limits the number of applications and operating systems that the file contents can be viewed in.
XLS is the old MS Excel format that was replaced by XLSX in Excel 2007.
* XLS files are binary, and therefore cannot be edited with a text editor, so either MS Excel, or another spreadsheet program that accepts XLS files as input
must be used to edit the files.
    
One potential solution would be to update __flexishow__ to also accept XLSX or CSV files, but that only potentially solves one problem. However, I have been
unable to locate the __flexishow__ source code. There are others:

* While Microsoft claims that XLSX is a standard, reality shows otherwise. Officially, XLSX is an open standard called Office Open XML, supposedly documented as standards ECMA-376 and ISO 29500. However, Microsoft only partially follows this standard and implements many proprietary, undocumented, additions that mean XLSX files cannot always be interchanged with other spreadsheet programs. In other words, while Microsoft was responsible for ramming Office Open XML through two standards organizations, they do not follow the standard themselves!
* While both __trilliumshowfx__ and __flexishow__ were written in Java, they use different GUI libraries, so they look very different. This can be quite jarring to users when switching from one program to the other. The user interface for neither program matches the graphical user interfaces of any of MS Windows, MacOS, or Gnome or KDE on Linux. It might be possible to change the UI of one or the other program, but the resulting UIs still are not native to the operating systems that the programs execute on.
* Only CSV files are allowed as input to __trilliumshowfx__. This limits the number of sources of image information available to the program.
* __Flexishow__ has not been updated in a number of years. I could not find the source code for the program, nor any way to generate an issue (bug report, change request, etc.).

## Status
### Development

Development of __tssconfig__ is just beginning, so at the moment, it is of limited to no use.

Initial development is being done on Linux (specifically KDE on TuxedoOS). Windows 11 and MacOS (Apple silicon only) versions will be provided when the Linux development is complete.
## Documentation
### License

__tssconfig__ is licensed under the MIT License. A copy of the license in included in this project's [LICENSE](LICENSE) file.

### Program Documentation

Documentation on how to use the program will be provided in this repository's Wiki when the first release of the program is created.
### Contributing Instructions

Instructions on how to contribute to __tssconfig__ are provided in [CONTRIBUTING.md](CONTRIBUTING.md).
### How to Build From Source

Instructions for building __tssconfig are provided in
[BUILDING.md](BUILDING.md). At the moment, only build instructions for
Debian-based Linux systems are given.
