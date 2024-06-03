# ConfigCreator
A Python script that generates a configuration file from a YAML template, dynamically creating corresponding Python classes and methods for easy configuration management.

[GitHub](https://github.com/clevrthings/ConfigCreator), [PyPi](https://pypi.org/project/ct-configcreator/)

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install ConfigCreator.

```bash
pip install pyyaml
pip install ct-configcreator
```

## Simple usage
```python
from ct_configcreator import createConfig

# Set the configuration file to load
template = "example_config.yaml"

# Set the output file to create. (Optional. Default = 'configuration.py')
output_file = "example_configuration.py"

# Create the python configuration file.
createConfig(template=template, output_file=output_file)
```

## Overview
This Python script provides functionality to generate a configuration file in Python from a YAML template. The script reads a YAML configuration file, dynamically creates corresponding Python classes, and generates a `` file with these classes, including methods for loading and initializing configuration values.

**Features:**
- Parses YAML configuration files.
- Dynamically generates Python classes based on the YAML structure.
- Creates a configuration.py file with generated classes and methods for loading YAML files.
- Includes logging for debugging and tracking the configuration generation process.

**Usage Example:**

**1. Prepare your YAML configuration file (e.g., example_config.yaml):**
```yaml
database:
  user:
    username: root
    password: password
  host: localhost
  port: 3306
logging:
  level: DEBUG
  file: app.log

cat1:
  sub1:
    sub2:
      sub3:
        sub4:
          sub5:
            sub6: Sub category 6 test
```
Notice you can use as many sub categories as you want.

**2. Run the script:**
```python
from ct_configcreator import createConfig

# Set the configuration file to load
template = "example_config.yaml"

# Set the output file to create. (Optional. Default = 'configuration.py')
output_file = "example_configuration.py"

# Create the python configuration file.
createConfig(template=template, output_file=output_file)
````


**3. The 'example_config.yaml' will look like this:**
```python
import yaml
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('Configuration')

def load_yaml(config_file):
    with open(config_file, 'r') as file:
        logging.info(f'Loaded {config_file} into config.')
        return yaml.safe_load(file)

class Config:
    def __init__(self, config_file):
        config = load_yaml(config_file)
        logging.debug("Initializing Config with config file")
        self.database = self.Database(config.get("database", {}))
        logging.debug("Initialized Config.database with nested config")
        self.logging = self.Logging(config.get("logging", {}))
        logging.debug("Initialized Config.logging with nested config")
        self.cat1 = self.Cat1(config.get("cat1", {}))
        logging.debug("Initialized Config.cat1 with nested config")
    __module__ = 'ct_configcreator.configcreator'
    class Database:
        def __init__(self, config):
            logging.debug("Initializing Database")
            self.user = self.User(config.get("user", {}))
            logging.debug("Initialized Database.user with nested config")
            self.host = config.get("host", 'localhost')
            logging.debug("Set Database.host to 'localhost'")
            self.port = config.get("port", 3306)
            logging.debug("Set Database.port to 3306")
        __module__ = 'ct_configcreator.configcreator'
        class User:
            def __init__(self, config):
                logging.debug("Initializing User")
                self.username = config.get("username", 'root')
                logging.debug("Set User.username to 'root'")
                self.password = config.get("password", 'password')
                logging.debug("Set User.password to 'password'")
            __module__ = 'ct_configcreator.configcreator'
            username = 'root'
            password = 'password'
            __doc__ = None
        host = 'localhost'
        port = 3306
        __doc__ = None
    class Logging:
        def __init__(self, config):
            logging.debug("Initializing Logging")
            self.level = config.get("level", 'DEBUG')
            logging.debug("Set Logging.level to 'DEBUG'")
            self.file = config.get("file", 'app.log')
            logging.debug("Set Logging.file to 'app.log'")
        __module__ = 'ct_configcreator.configcreator'
        level = 'DEBUG'
        file = 'app.log'
        __doc__ = None
    class Cat1:
        def __init__(self, config):
            logging.debug("Initializing Cat1")
            self.sub1 = self.Sub1(config.get("sub1", {}))
            logging.debug("Initialized Cat1.sub1 with nested config")
        __module__ = 'ct_configcreator.configcreator'
        class Sub1:
            def __init__(self, config):
                logging.debug("Initializing Sub1")
                self.sub2 = self.Sub2(config.get("sub2", {}))
                logging.debug("Initialized Sub1.sub2 with nested config")
            __module__ = 'ct_configcreator.configcreator'
            class Sub2:
                def __init__(self, config):
                    logging.debug("Initializing Sub2")
                    self.sub3 = self.Sub3(config.get("sub3", {}))
                    logging.debug("Initialized Sub2.sub3 with nested config")
                __module__ = 'ct_configcreator.configcreator'
                class Sub3:
                    def __init__(self, config):
                        logging.debug("Initializing Sub3")
                        self.sub4 = self.Sub4(config.get("sub4", {}))
                        logging.debug("Initialized Sub3.sub4 with nested config")
                    __module__ = 'ct_configcreator.configcreator'
                    class Sub4:
                        def __init__(self, config):
                            logging.debug("Initializing Sub4")
                            self.sub5 = self.Sub5(config.get("sub5", {}))
                            logging.debug("Initialized Sub4.sub5 with nested config")
                        __module__ = 'ct_configcreator.configcreator'
                        class Sub5:
                            def __init__(self, config):
                                logging.debug("Initializing Sub5")
                                self.sub6 = config.get("sub6", 'Sub category 6 test')
                                logging.debug("Set Sub5.sub6 to 'Sub category 6 test'")
                            __module__ = 'ct_configcreator.configcreator'
                            sub6 = 'Sub category 6 test'
                            __doc__ = None
                        __doc__ = None
                    __doc__ = None
                __doc__ = None
            __doc__ = None
        __doc__ = None
    __doc__ = None
```

**4. Use the configuration in your main code:**
```python
from example_configuration import Config

# Initialise the config file and load the newest values from the file
config = Config("example_config.yaml")

# Access the config values examples
print(config.database.user.password)
print(config.logging.file)
print(config.cat1.sub1.sub2.sub3.sub4.sub5.sub6)
```
The initialization will always read the latest values from the config file, so the original values in the config file when `configuration.py` was created do not matter.

**5. This example will output the following:**
```
>>> password
>>> app.log
>>> Sub category 6 test
```

# Contributing
Contributions are welcome! Please open an issue or submit a pull request on GitHub.
You can also suggest a new sensor by opening an issue. 

# Support my work
If you like my work you can always [buy me a coffee!](https://buymeacoffee.com/clevrthings)