# Contributing Guidelines
## How to contribute
The HCC Workshop is designed to showcase all of the varied research areas pursued by the HCC research group. Activities around each of the different research areas are essential for ensuring the HCC Workshop is engaging and attracts a diverse range of interests. While diversity is encouraged, to ensure consistency and future development, there are a few guidelines that contributors should follow. 
## Core vs modules
The HCC Workshop consists of several modular applications that build from a core base. New functionality is typically directed toward modules to ensure a functional and lightweight workshop core. Unless your material is specifically related to existing modules, all new content should be built into a new application. If you are unsure of whether your contribution should be implemented as a module of part of the HCC Workshop core, ask the development team for advice.  
## Pushing changes to master
As the master branch is currently used in production on the HCC Web Server, pushing is disabled for all developers in order to protect the site's integrity and functionality. 
When finished developing new functionality, create a merge request in order for the code to be reviewed and added to the master branch. To increase the likelihood that a merge request is accepted, please follow the following guidelines.
## General development guidelines
* Do **not** work directly on the master branch. Always create a new branch to work with by using `git checkout -b new-branch`
* Use python 3.5 and jQuery 2.2.4 only.
* Extend the core base.html files
* Extend the core theme.css files
* Write legible, code with logical variable and function names. Your code should contain at least 35% comments
* Stick to python PEP 8 conventions wherever possible
* Make commits of logical units with sensible commit messages
* Check for unnecessary whitespace with `git diff --check` before committing
* When making commits, be as descriptive as possible as to what changes you are making and why
* Ensure that your changes have not broken any existing functionality. Run your own tests in your own offline development environment to make sure
* Read the Django documentation and do the tutorials to help you
* Most importantly, please ask questions and discuss with the rest of the development team if you are unsure about anything

## Raising issues
* Check that another ticket describing the same issue does not already exist
* Clearly describe the issue including steps to reproduce it when it is a bug
* Be as descriptive as possible as to what you think requires changing and why

## Further information
* [PEP 8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/) 
* [Django 1.9.8](https://docs.djangoproject.com/en/1.9)