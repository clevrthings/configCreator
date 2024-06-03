from example_configuration import Config

# Initialise the config file and load the newest values from the file
config = Config("example_config.yaml")

# Access the config values examples
print(config.database.user.password)
print(config.logging.file)
print(config.cat1.sub1.sub2.sub3.sub4.sub5.sub6)