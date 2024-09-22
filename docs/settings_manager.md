# Settings Manager

`settings_manager` is a versatile and modular frontend designed for managing configuration files in JSON format. It interacts seamlessly with the backend library `globalcfg`, which handles the reading and writing of the configuration file. The module is independent and can be extended or adapted for other projects, all under the same GPL license as the original project.


![screenshot](/screenshots/settings.png)


## How `settings_manager` Retrieves and Reads the Settings

## Overview

The `settings_manager` module is designed to read configuration settings from a JSON file. It provides a flexible and reliable way to manage settings, regardless of how many key-value pairs the configuration file contains. 

## Where the Configuration File is Stored

By default, the configuration file is a simple JSON file stored locally on '/cfg/settings.json'. 

If you want to chage it, edit the net line in global_cfg.py:
```python
 self.settings_file='cfg/settings.json'
 ```



## Features

- **Frontend for JSON configuration management**: Provides a simple and user-friendly way to modify and manage JSON configuration files.
- **Integration with `globalcfg`**: Automatically handles reading from and saving to JSON configuration files using the `globalcfg` library.
- **Modular and reusable**: Can be easily adapted to other projects that require configuration management.
- **Extensible**: Can be extended with custom functions and configuration options based on project needs.

## Installation

Just Copy **settings_manager.py** and **/components/global_cfg.py** to yout project an run

If you want to use a diferent path for **global_cfg.py**, you need to edit the next line in **settings_manager.py**, just chage **components** for another path or erase it with the point to use the same directory than **settings_manager.py**

```python
from components.global_cfg import GlobalCfg
```

Finally to run it:
```bash
python settings_manager.py
```

## Importing the Module in your app
First, import the necessary components:

```python
from settings_manager import SettingsManager
```

## Initializing the Settings Manager
Create an instance of the SettingsManager, specifying the path to the configuration file.

```python
config_file_path = "config.json"
settings = SettingsManager(config_file_path)
```
## Loading Configuration
To load the settings from the configuration file:
```python
settings.load_settings()
```
This will read the configuration data from the JSON file and load it into the manager.

## Load settings from JSON file
```python
config = globalcfg.load_config("config.json")
```
Example of JSON settings file

```json
{
    "username": "default_user",
    "theme": "dark",
    "notifications": true,
    "language": "en"
}
```

### License
settings_manager is licensed under the GNU General Public License (GPL). This ensures that:

The software is free to use, modify, and distribute.
Any modifications made to the codebase must be atributed and shared under the same license.
For more details on licensing, refer to the GPL License.


# Contact
For questions, suggestions, or issues, please reach out through our [GitHub](https://github.com/neocronos666) repository or join our Discord server:
- 🇬🇧 [English bug report discord channel](https://discord.gg/4Dnd5CeYFy)
- 🇪🇸 [Canal de discord en Español para reporte de errores](https://discord.gg/ZbEu5cwzkJ)

## Author
[***Sergio Silvestri***](https://github.com/neocronos666) - Original developer
Feel free to reach out for collaboration or feature requests!

