# Open CheatSheet Public-Alpha v0.18

> **Enhance your study efficiency with Open CheatSheet**: Instantly access all your necessary formulas and tips, distraction-free and without ads, right from your phone or any device. Open CheatSheet is designed to help students focus and retain productivity by keeping all the formulas, constants, and tips in one place—without the need for an internet connection.

---
![screenshot](/screenshots/main.jpg)
---
## Why Open CheatSheet?

In today’s digital world, students often turn to the internet to look up formulas or quick references. Unfortunately, this opens the door to distractions such as ads, social media, or unrelated content. This results in wasted time and loss of concentration. **Open CheatSheet** solves this problem by providing an offline, fast, and distraction-free reference tool where students can access all the essential formulas and tricks they need in their studies or games.

Whether you're working on a complex math problem or need a quick reminder of game tips, Open CheatSheet is the companion app designed to boost your productivity without interruptions.

---

## Key Features

- **Offline Access**: All necessary formulas and tricks are available at your fingertips, even without an internet connection.
- **Multi-platform & Adaptive**: Available for Android, iOS, Windows, macOS, Linux, and Raspberry Pi. It is designed to work smoothly on any device.
- **Designed for Students & Teachers**: Easy to use, accessible, and adaptable. Future updates will include sharing and printing functionality to assist educators and students alike.
- **Fully Open Source**: Contributions from the community are welcomed and encouraged. The project is managed via GitHub.

---

## What is Open CheatSheet?

**Open CheatSheet** is a Python-based application that organizes and provides essential formulas, constants, and tips in a structured, easy-to-access format. The app is inspired by mobile-first design but is built to function natively across all major platforms. The app's goal is to eliminate the distractions that come with online searches, focusing instead on delivering fast, relevant information offline. It’s lightweight, fast, and created with **flet** to ensure that it runs smoothly on any device.

## Roadmap

#### Stay updated by checking our Roadmap for detailed information on upcoming features and timelines.

### :baby: Pre-Alpha
- [*] Design front-end
- [*] Create minimum controls
- [*] Add Favs
- [*] Add Lists
- [*] Implement Navigation
- [*] Implment URL navigation
- [*] Create [Settings Manager](/docs/settings_manager.md) Tool
- [*] Create [Get Requirements](/docs/get_requirements.md) Tool
- [*] Create about screen
- [*] Write documentation
- [*] Private tests
- [*] debug
- Open to Suggestions

### :boy: Public-Alpha
- [*] Public Alpha Release
- [ ] Create new ChSheet
- [ ] Search in Buffer
- [ ] Imporove Interface
- [ ] Implement Dark/light theme
- [ ] Autodetect platform theme
- [ ] MULTI LANG SUPPORT
- Open to issues and suggestions

### :man: Public-Beta
- [ ] create all platforms package installer
- [ ] Study the chance to get a server and post an free online version of the app
- [ ] Implement autoupdate protocol
- [ ] Agregar funciones con ayuda de la comunidad
- Open to issues and suggestions

### :suspect: Release
- [ ] Upload packages to repos
- Open to issues and suggestions

### :vulcan_salute: Branching
- [ ] Study branches to create using the format, like for videogames cheats or cook recipes.
- [ ] Create an online test version
- Open to issues and suggestions

### Current State

Currently, the app is in **Public-Alpha** development, with testing primarily done on desktop platforms. However, the goal is to release it for all supported platforms once the development stabilizes.

---

## What is a .chsheet file?

Open CheatSheet uses files with the `.chsheet` extension to store formulas, constants, and explanations in a structured format. Here’s what a typical file contains:

- **Title**: The name of the formula or concept.
- **Brief Description**: A short description summarizing the concept.
- **Detailed Explanation**: A more detailed, multi-paragraph explanation with support for lists and LaTeX-like formatting for formulas.
- **Formula(s)**: The primary formula written in LaTeX syntax.
- **Variables Table**: A table explaining the variables used in the formula.
- **Constants Table**: A table of constants with their values and descriptions.
- **Images**: An optional image related to the concept (e.g., diagrams, charts, etc.).
- **References**: Links to websites that provide more in-depth information on the topic.
- **Related Formulas**: Links to other related `.chsheet` files.



---

# Installation
Open CheatSheet is developed primarily in Python and uses flet for the graphical interface, ensuring it runs natively across all platforms.

To get started with Open CheatSheet on your machine:

Clone the repository:

```bash
git clone https://github.com/yourusername/open-cheatsheet
```
Install the required dependencies:


```bash
pip install -r requirements.txt
```
Run the app:

```bash
python main.py
```
### Supported Platforms

The app is designed to be adaptable and available across multiple platforms:

- Android
- iOS
- Windows
- macOS
- Linux
- Raspberry Pi

**We plan to release installation packages for all platforms soon.**

### How to Contribute
We're building this project as a community effort, and we need your help to take Open CheatSheet to the next level!

Areas of Contribution:
- **Content Creation:** We need students, educators, and professionals to help expand the database of formulas.
- **Design:** Help us create clean and intuitive graphics and diagrams for the formulas.
- **Programming and Testing:** Test the app across different platforms, contribute code, and help us optimize the app for better performance.

We will be adding detailed guides for contributors in the Docs section, so stay tuned! 
All collaboration is managed through GitHub and Discord (more info see [how_to_contribute](docs/how_to_contribute.md)).



---

## Documentation
- [FAQ](docs/faq.md)
- [CheatSheets format](docs/ES_chsheet_format.md)
- [CheatSheets Examples](docs/ES_chsheet_examples.md)
- [Known installation problems](docs/solved.md)
- [Get Requirement Tools](docs/get_requirements.md)
- [Settings Manager Tools](docs/settings_manager.md)
- [HOW TO CONTRIBUTE](docs/how_to_contribute.md)

## Licensing
This project is licensed under the GPL (General Public License), meaning it's free for personal and educational use, and anyone who modifies the code must give proper credit and may not use it for commercial purposes.



## Reach Contact
- 🇬🇧 [English bug report discord channel](https://discord.gg/4Dnd5CeYFy)
- 🇪🇸 [Canal de discord en Español para reporte de errores](https://discord.gg/ZbEu5cwzkJ)

## Donations (Soon)
Love the project and want to support us? Consider making an anonymous donation. Your contribution will help us keep the project free, open-source, and available to students worldwide!

Thank you for your support!






