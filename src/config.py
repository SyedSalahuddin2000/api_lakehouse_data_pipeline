import yaml

def load_config():
    with open("config/config.yaml","r") as f:
        yaml_data = yaml.safe_load(f)
    return yaml_data