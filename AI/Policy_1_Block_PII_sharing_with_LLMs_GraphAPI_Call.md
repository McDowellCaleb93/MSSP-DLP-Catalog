### Graph API Call Sample for Block PII sharing with LLMs

**Request URL:**
```
POST https://graph.microsoft.com/v1.0/security/dataLossPreventionPolicies
```

**Request Headers:**
```
Authorization: Bearer <YOUR_ACCESS_TOKEN>
Content-Type: application/json
```

**Request Body:**
```json
{
    "displayName": "Block PII sharing with LLMs",
    "description": "Prevent PII data from being input into AI tools.",
    "isEnabled": true,
    "mode": "enforce",
    "priority": 1,
    "rules": [
        {
            "id": "rule-47591",
            "name": "Block PII sharing with LLMs",
            "actions": [
                {
                    "type": "blockAccess"
                }
            ],
            "conditions": {
                "contentContainsSensitiveInformation": [
                    {
                        "sensitiveTypeId": "general-pii-sit",
                        "minCount": 1,
                        "confidenceLevel": "high"
                    }
                ],
                "contentContainsAnyOfWords": [
                    "ChatGPT",
                    "Copilot",
                    "LLM",
                    "OpenAI",
                    "Claude",
                    "Gemini",
                    "Anthropic",
                    "Bard",
                    "GPT-4",
                    "GPT-3.5"
                ]
            },
            "locations": [
                "Exchange",
                "Teams",
                "OneDrive",
                "SharePoint",
                "Endpoint"
            ],
            "userNotification": {
                "isEnabled": true,
                "templateId": "default-notification-template"
            },
            "incidentReport": {
                "isEnabled": true,
                "recipients": [
                    "ai-dlp-alerts@company.com"
                ]
            }
        }
    ]
}
```