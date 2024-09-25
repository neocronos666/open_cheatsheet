# .chlist File Documentation

## Overview

The `.chlist` file is a custom file format used to store a list of relative paths to `.chsheet` files, without their extensions. These files are essential for organizing and managing groups of `.chsheet` files within the project.

## File Structure

Each `.chlist` file contains one `.chsheet` entry per line, representing a relative path to a `.chsheet` file inside `/cheatsheets/` path. The entries do not include the `.chsheet` extension.

### Example

```plaintext
maths/calculus/derivative table
physics/dynamics/energy and work
chemistry/atomic models/bohr's atomic model
```
In this example, each line points to a `.chsheet` file located at the specified relative path. The actual filenames would be:
- (app_path)/cheatsheets/maths/calculus/derivative table.chsheet
- (app_path)/cheatsheets/physics/dynamics/energy and work.chsheet
- (app_path)/cheatsheets/chemistry/atomic models/bohr's atomic model.chsheet

## Favs .chlist File: .favs.chlist

A hidden `.chlist` file, named `.favs.chlist`, is located in the `/lists/` directory. This file stores a list of favorite `.chsheet` files and is used to quickly access frequently used or important sheets.



