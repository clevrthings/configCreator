import yaml
import logging
from typing import Any, Dict, Type

class BaseConfig:
    pass

add_load_yaml = False
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('GenerateConfigFile')

def createConfig(template: str, output_file: str = "configuration.py"):
    def recursive_class_creation(name: str, data: Dict[str, Any]) -> Type:
        class_dict = {"__module__": __name__}
        for key, value in data.items():
            if isinstance(value, dict):
                nested_class = recursive_class_creation(key.capitalize(), value)
                class_dict[key] = nested_class
            else:
                class_dict[key] = value
        return type(name, (BaseConfig,), class_dict)

    with open(template, 'r') as file:
        yaml_data = yaml.safe_load(file)
        logging.debug(f"Loaded YAML data: {yaml_data}")

    Config = recursive_class_creation("Config", yaml_data)
    generate_python_file(Config, yaml_data, output_file)

def generate_python_file(Config: Type, yaml_data: Dict[str, Any], output_file: str):
    def write_class(class_obj: Type, class_name="Config", yaml_data=yaml_data, indent=0):
        lines = []
        indent_str = "    " * indent

        def add_init_method(yaml_section, indent):
            global add_load_yaml
            init_lines = []
            indent_str = "    " * (indent + 1)
            if not add_load_yaml:
                init_lines.append(f"{indent_str}def __init__(self, config_file):")
                init_lines.append(f"{indent_str}    config = load_yaml(config_file)")
                init_lines.append(f"{indent_str}    logging.debug(\"Initializing {class_name} with config file\")")
                add_load_yaml = True
            else:
                init_lines.append(f"{indent_str}def __init__(self, config):")
                init_lines.append(f"{indent_str}    logging.debug(\"Initializing {class_name}\")")
            for key, value in yaml_section.items():
                if isinstance(value, dict):
                    init_lines.append(f"{indent_str}    self.{key} = self.{key.capitalize()}(config.get(\"{key}\", {{}}))")
                    init_lines.append(f"{indent_str}    logging.debug(\"Initialized {class_name}.{key} with nested config\")")
                else:
                    init_lines.append(f"{indent_str}    self.{key} = config.get(\"{key}\", {repr(value)})")
                    init_lines.append(f"{indent_str}    logging.debug(\"Set {class_name}.{key} to {repr(value)}\")")
            return init_lines

        lines.append(f"{indent_str}class {class_name}:")
        attributes = class_obj.__dict__.items()
        if not attributes:
            lines.append(f"{indent_str}    pass")
        else:
            init_method_lines = add_init_method(yaml_data, indent)
            lines.extend(init_method_lines)

            for attr_name, attr_value in attributes:
                if isinstance(attr_value, type):
                    nested_class_yaml_data = yaml_data.get(attr_name.lower(), {})
                    nested_class_lines = write_class(attr_value, attr_name.capitalize(), nested_class_yaml_data, indent + 1)
                    lines.extend(nested_class_lines)
                else:
                    lines.append(f"{indent_str}    {attr_name} = {repr(attr_value)}")
        return lines

    def write_load_yaml_function(indent=0):
        lines = [
            "import yaml",
            "import logging",
            "",
            "logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')",
            "logger = logging.getLogger('Configuration')",
            "",
            "def load_yaml(config_file):",
            "    with open(config_file, 'r') as file:",
            "        logging.info(f'Loaded {config_file} into config.')",
            "        return yaml.safe_load(file)",
            "",
        ]
        return lines

    load_yaml_function_lines = write_load_yaml_function()
    main_class_lines = write_class(Config)
    lines = load_yaml_function_lines + main_class_lines

    with open(output_file, 'w') as file:
        file.write("\n".join(lines))
        logging.info("configuration.py created")

# Example usage:
if __name__ == "__main__":
    createConfig("config.yaml", "configuration.py")
