import json
import os
import sys

def load_client_config(config_path):
    with open(config_path, 'r') as f:
        return json.load(f)

def process_template(policy_path, client_config, output_path):
    with open(policy_path, 'r') as f:
        policy = f.read()

    # Replace placeholders with client-specific values
    for key, value in client_config.items():
        placeholder = f"{{{{{key}}}}}"
        if isinstance(value, list):
            value = json.dumps(value)  # Convert lists to JSON arrays
        elif isinstance(value, dict):
            value = json.dumps(value)  # Convert dicts to JSON objects
        else:
            value = str(value)
        policy = policy.replace(placeholder, value)

    # Save the processed policy
    with open(output_path, 'w') as f:
        f.write(policy)

    print(f"Processed policy saved to: {output_path}")

def process_all_policies(policy_folder, client_config, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    for root, _, files in os.walk(policy_folder):
        for file in files:
            if file.endswith('.json'):
                policy_path = os.path.join(root, file)
                relative_path = os.path.relpath(policy_path, policy_folder)
                output_path = os.path.join(output_folder, relative_path)
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                process_template(policy_path, client_config, output_path)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python dlp_template_processor.py <client-config.json> <policy-folder> <output-folder>")
        sys.exit(1)

    config_file = sys.argv[1]
    policy_dir = sys.argv[2]
    output_dir = sys.argv[3]

    print(f"Loading client configuration from: {config_file}")
    client_config = load_client_config(config_file)

    print(f"Processing policies in: {policy_dir}")
    process_all_policies(policy_dir, client_config, output_dir)
    print("All policies processed successfully.")