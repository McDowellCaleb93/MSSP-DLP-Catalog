### Graph API Call Sample for Audit merger and acquisition data

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
    "displayName": "Audit merger and acquisition data",
    "description": "Monitor M&A data movement.",
    "isEnabled": true,
    "mode": "test",
    "priority": 1,
    "rules": [
        {
            "id": "rule-50083",
            "name": "Audit merger and acquisition data",
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
                "contentContainsAnyOfWords": []
            },
            "locations": [
                "Exchange",
                "Teams",
                "OneDrive",
                "SharePoint"
            ],
            "userNotification": {
                "isEnabled": true,
                "templateId": "default-notification-template"
            },
            "incidentReport": {
                "isEnabled": true,
                "recipients": [
                    "dlp-alerts@company.com"
                ]
            }
        }
    ]
}
```