import yaml
import subprocess

# Load the YAML file
with open('file.yml', 'r') as stream:
    data = yaml.safe_load(stream)

# Extract the bash lines from before_script, script, and after_script
bash_lines = []
for key in ['before_script', 'script', 'after_script']:
    if key in data['package']:
        bash_lines += data['package'][key]

# Pass the bash lines to shellcheck
for line in bash_lines:
    result = subprocess.run(['shellcheck', '-s', 'bash', '-e', 'SC2148', '-x', line], capture_output=True)
    print(result.stdout.decode())
