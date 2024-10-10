# This is a prototype prompt to make .chseet files in much AI's
## Just copy/paste from the next line, and add to the end the required field

---

We will now create .chsheet files. These files are JSON-based, and they follow this structure:

{
    "title": "Topic Title",
    "description": "Brief description of the topic",
    "detail": "<markup>Detailed description, which may include HTML or markup</markup>",
    "img": "An image related to the topic",
    "forms": "Formula in LaTeX format",
    "var_table": [
        {"var": "variable_name", "desc": "Description of the variable used in the image"}
    ],
    "cons_table": {
        "headers": [
            "Constant",
            "Value",
            "Description"
        ],
        "rows": [
            {
                "constante": "g",
                "valor": "9.81 m/s &sup2;",
                "descripcion": "Gravity acceleration"
            }
        ]
    },
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
        "Default", 
        "dark"
    ]
}


Main Types of .chsheet Files:

Formula Sheets: Contain a title, a 2-line text description, a theoretical detail (in markup format), an image, the formula (in LaTeX format), and a small reference table for the variables used in the formula (with units, if necessary).
Table Sheets: Contain a title, a brief text description (a few lines), and a table of constants (in HTML format).
Custom Sheets: These can combine elements from both formulas and tables or even include multiple elements of the same type (e.g., more than one table or image).
Each .chsheet file will be referred to as a "sheet." The idea is that it includes all relevant information for a particular formula or concept.

Administrative Fields:All sheets will include administrative fields such as:

Creation date,
Last modification date,
Author's name, email, and website,
A list of useful reference websites (such as Wikipedia),
A list of related formulas, which links to other .chsheet files within the app.
Template Compatibility: Each sheet will also have a field indicating which templates are compatible. For now, all will use the default template.

File Naming and Organization:
The file name and location of each .chsheet file is important. Files are located in the /cheatsheets directory, and subdirectories represent categories and subcategories. Each .chsheet file is a single sheet.

The file naming convention is as follows: /cheatsheets/[category]/[subcategory]/[LANGUAGE_CODE]_[formula_name].chsheet
Where LANGUAGE_CODE is a two-letter code indicating the language (e.g., ES for Spanish). 
For example:/cheatsheets/physics/kinematics/ES_Motion_in_a_straight_line.chsheet

Extra Notes:
- The image field will always be named following this convention: "formula_name.jpg", using the title of the formula as the image name.
- The formula title should match textbook conventions and be as simple as possible.
- In some prompts, we may create multiple sheets at once, with each sheet enclosed in a separate code block.
- Responses should be concise, providing only the necessary JSON code and any minimal additional instructions.

With all the information given let's create a .chsheet, I'll give you some info and you have to complete (if needed):

Sheet type: Formula sheet / table sheet (pick one)
Language: EN/ES/FR/JP (choose one or edit to ask for more, well splitted)
Title: (pick a tittle)
Description: (not necessary for formula sheets, but some table sheet may need it)
