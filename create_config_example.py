from ct_configcreator import createConfig

# Set the configuration file to load
template = "example_config.yaml"

# Set the output file to create. (Optional. Default = 'configuration.py')
output_file = "example_configuration.py"

# Create the python configuration file.
createConfig(template=template, output_file=output_file)