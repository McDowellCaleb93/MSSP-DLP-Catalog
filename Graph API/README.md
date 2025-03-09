# DLP Policy Templating Tool

## Overview

This Python tool enables **real-time client-specific templating** for Microsoft DLP policies. It reads client-specific configurations and automatically replaces placeholders inside policy JSON templates, generating ready-to-deploy policies for Microsoft Graph API.

## 📦 Files Included

- `dlp_template_processor.py`: Main Python script for processing templates.
- `client-config.json`: Example client configuration file (you should create one per client).
- `README.md`: This file.

## ⚙️ How It Works

The tool will:
1. Load client-specific configurations from `client-config.json`.
2. Read all `.json` policy templates from a given folder.
3. Replace placeholders like `{{incidentRecipients}}`, `{{dlpNotificationTemplateId}}`, etc., using the client configuration.
4. Output fully processed, client-specific DLP policies in an output folder — ready for deployment via Graph API or automation pipelines.

## 🔑 Placeholders Format

Placeholders inside policy templates should be wrapped with double curly braces `{{ }}`.

### Example in Policy Template:
```json
{
  "recipients": {{incidentRecipients}},
  "templateId": "{{dlpNotificationTemplateId}}"
}
```

### Example in Client Config:
```json
{
  "incidentRecipients": ["security@acme.com", "compliance@acme.com"],
  "dlpNotificationTemplateId": "template-123456"
}
```

### Resulting Output:
```json
{
  "recipients": ["security@acme.com", "compliance@acme.com"],
  "templateId": "template-123456"
}
```

## 🚀 How to Use

### Step 1: Prepare Client Configuration

Create a `client-config.json` file with client-specific values:
```json
{
  "clientName": "Acme Corp",
  "tenantId": "1234-5678-9101-1121",
  "complianceEmails": ["compliance@acme.com"],
  "trustedDomains": ["acme.com", "partner.acme.com"],
  "dlpNotificationTemplateId": "template-123456",
  "incidentRecipients": ["security@acme.com", "legal@acme.com"]
}
```

### Step 2: Prepare Policy Templates

Ensure that policy JSON files in your policy folder contain placeholders where client-specific data should be injected.

### Step 3: Run the Script

```bash
python dlp_template_processor.py client-config.json ./Policies ./Output
```

- `client-config.json`: Path to your client config file.
- `./Policies`: Folder containing template policies.
- `./Output`: Destination folder where ready-to-deploy client policies will be saved.

### Example Command:
```bash
python dlp_template_processor.py client-config.json ./Healthcare ./Client_Acme_Healthcare_Policies
```

## 📂 Output

- Output folder will contain fully processed DLP policy JSON files specific to that client.
- Ready to deploy using Graph API, PowerShell, or automation pipelines.

## ✅ Benefits

- **Dynamic**: One master template for all clients, dynamically customized.
- **Scalable**: Quickly generate policies for many clients.
- **Automated**: No manual adjustments — ready for CI/CD pipelines.

## 💡 Example Workflow

1. **Prepare** client-config.json
2. **Run** `dlp_template_processor.py`
3. **Deploy** output using PowerShell or GitHub Actions pipeline.

## 🚀 Future Improvements

- [ ] Add Jinja2 for advanced templating (loops, conditionals).
- [ ] Integrate directly into GitHub Actions workflow.
- [ ] Add policy validation step.

---

**Author**: Security Services Division