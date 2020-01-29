# Password Manager
## Basic Information
**Author**: [*lightningb4*](https://github.com/gregoryerik)

**Date Created**: *31/12/2019*

**Last Updated**: *11/01/2020*

**Version**: *0.1*


_Python 3.7.5 was used for the development of this project_

## Requirements
| Name|Version  |
|--|--|
| SQLAlchemy | 1.3.12 |
| cryptography | 2.8 |
| PyQRCode | 1.2.1 |
| Pillow | 6.1.0 |
| pypng | 0.0.20 |
| pyperclip | 1.7.0 |
|termcolor |1.1.0 |

## Setup

After downloading the project install the requirements
```
python3 -m pip install requirements.txt --user
```
Once that has completed:

Rename the __default_config.json__ file to __config.json__ 
```
python3 passwordmanager.py
```
The warnings of the database deletion are present as a backup method for wiping the applications memory and restarting is editing the configuration file
to load setup in first time mode. However, a last resort safety feature is to warn the user before they potentially delete all of their passwords.

## Suggestions

If you continue to use this program on a regular basis, consider creating a custom bash command to run the program from the terminal easily.

## TODO

- Update the main file to use the prefixes instead of hard coding each colour. Possibly add new prefixes for that use
- Pillow issue with current version
- Implement logger