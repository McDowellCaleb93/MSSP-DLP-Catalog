# Templating Approach for Client-Specific Policies

## Example Placeholder in Policy JSON:
```
"recipients": ["{{incidentRecipients}}"],
"templateId": "{{dlpNotificationTemplateId}}"
```

## Templating Process (Python/Powershell):
1. Load client-config.json
2. For each policy JSON file, replace placeholders like {{incidentRecipients}} and {{dlpNotificationTemplateId}} with real values.
3. Save or deploy the final policy.

## Example Python Snippet for Templating:
```python
import json

# Load client config
with open('client-config.json', 'r') as f:
    client_config = json.load(f)

# Load and replace placeholders in a policy file
with open('policy.json', 'r') as f:
    policy = f.read()

# Replace placeholders
for key, value in client_config.items():
    placeholder = f"{{{{{key}}}}}"  # e.g., {{incidentRecipients}}
    if isinstance(value, list):
        value = json.dumps(value)
    policy = policy.replace(placeholder, value)

# Save updated policy
with open('policy_final.json', 'w') as f:
    f.write(policy)
```

## Benefits:
- One master template per policy, reused across clients.
- Dynamic, scalable deployments without maintaining separate copies per client.