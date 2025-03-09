### Graph API Call Sample for Block Legal Documents sharing with LLMs

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
    "displayName": "Block Legal Documents sharing with LLMs",
    "description": "Prevent legal documents from being input into LLMs.",
    "isEnabled": true,
    "mode": "enforce",
    "priority": 1,
    "rules": [
        {
            "id": "rule-17781",
            "name": "Block Legal Documents sharing with LLMs",
            "actions": [
                {
                    "type": "blockAccess"
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