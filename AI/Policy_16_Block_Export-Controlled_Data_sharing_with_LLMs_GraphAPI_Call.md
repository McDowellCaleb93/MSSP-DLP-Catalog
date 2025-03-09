### Graph API Call Sample for Block Export-Controlled Data sharing with LLMs

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
    "displayName": "Block Export-Controlled Data sharing with LLMs",
    "description": "Prevent export-restricted data leakage via AI tools.",
    "isEnabled": true,
    "mode": "enforce",
    "priority": 1,
    "rules": [
        {
            "id": "rule-38086",
            "name": "Block Export-Controlled Data sharing with LLMs",
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