import yaml

#load the config from config.yaml file
def load_config():
    with open("config/config.yaml","r") as f:
        yaml_data = yaml.safe_load(f)
    return yaml_data