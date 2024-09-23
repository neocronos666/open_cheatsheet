# How to Create `.chsheet` Files

This guide explains how to create `.chsheet` files, which are JSON-based files used to store formulas, constants, and other data relevant to a specific topic. These files are structured to be easily interpreted by both humans and machines, following the format outlined below.

Note: you can use a [given prompt](chseet_prompt.md) to make it with som AI,

## File Structure

Each `.chsheet` file follows a standard JSON structure:

```json
{
    "title": "Topic Title",
    "description": "Brief description of the topic",
    "detail": "<markup>Detailed description, which may include HTML or markup</markup>",
    "img": "An image related to the topic",
    "forms": "Formula in LaTeX format",
    "var_table": [
        {"var": "variable_name", "desc": "Description of the variable used in the image"}
    ],
    "cons_table": [
        {"constante": "constant_name", "value": "value", "description": "Description for large data tables"}
    ],
    "c_date": "Creation date of the file",
    "m_date": "Last modification date",
    "author": "Author's name",
    "email": "Author's email",
    "web": "Author's website",
    "ref_webs": [
        "Reference URL 1",
        "Reference URL 2"
    ],
    "rel_forms": [
        "Related .chsheet file name"
    ],
    "template": [
        "default"
    ]
}
```

## Types of .chsheet Files

### Formula Sheets:

Include the title, a brief description (2 lines), detailed theory (markup), a related image, a formula in LaTeX, and a small table of variables with descriptions.

### Table Sheets:

Include a title, short description, and a constant table in HTML format.

### Custom Sheets:

These can combine elements from both formulas and tables or have multiple of the same type (e.g., more than one table or image).
Naming and Directory Structure
Each **.chsheet** file is stored in the **/cheatsheets** directory. Subdirectories represent categories and subcategories. The file naming convention is:

```css
/cheatsheets/[category]/[subcategory]/[LANGUAGE_CODE]_[formula_name].chsheet
```

Where **LANGUAGE_CODE** is a two-letter code indicating the language (e.g., ***ES*** for Spanish). For example:

For example:

```bash
/cheatsheets/physics/kinematics/'EN_Motion in a straight line.chsheet'
```
## Administrative Fields

Each **.chsheet** contains the following metadata fields:

- **c_date:** Creation date.
- **m_date:** Last modification date.
- **author data:** Name, email, and website of the author. Note if you made the chsheet file wit IA, you sould add you name as "Your name [Using ChatGPT4]"
- **ref_webs:** A list of reference websites where the data came, usually a wikipedia url.
- **rel_forms:** A list of related .chsheet files within the app.
- **template:** Defines the compatible templates (default, dark, etc.), for now all shoud have "default" only.

## How to Contribute
For contributions, such as creating .chsheet files or suggesting new features, please refer to our [Contribution Guidelines](how_to_contribute.md).