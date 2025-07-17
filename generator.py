import yaml

def load_blueprint(file):
    with open(file, 'r') as f:
        return yaml.safe_load(f)

def generate_pipeline(config):
    steps = []

    if config['stack'] == 'python':
        steps.append('templates/_build-python.yml')
    elif config['stack'] == 'java':
        steps.append('templates/_build-java.yml')

    if config.get('security_scan'):
        steps.append('templates/_security.yml')

    if config['deployment'] == 'docker':
        steps.append('templates/_deploy-docker.yml')

    return steps

if __name__ == "__main__":
    config = load_blueprint('blueprint.yaml')
    pipeline = generate_pipeline(config)

    print("Templates to include:")
    for step in pipeline:
        print(f" - {step}")
