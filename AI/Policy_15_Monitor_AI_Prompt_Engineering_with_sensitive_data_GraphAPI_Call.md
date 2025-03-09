### Graph API Call Sample for Monitor AI Prompt Engineering with sensitive data

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
    "displayName": "Monitor AI Prompt Engineering with sensitive data",
    "description": "Audit sensitive prompts to AI tools.",
    "isEnabled": true,
    "mode": "test",
    "priority": 1,
    "rules": [
        {
            "id": "rule-69473",
            "name": "Monitor AI Prompt Engineering with sensitive data",
            "actions": [
                {
                    "type": "audit"
                }
            ],
            "conditions": {
                "contentContainsSensitiveInformation": [
                    {
                        "sensitiveTypeId": "general-confidential-data-sit",
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