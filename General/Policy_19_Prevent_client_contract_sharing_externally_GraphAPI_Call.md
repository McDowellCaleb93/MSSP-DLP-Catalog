### Graph API Call Sample for Prevent client contract sharing externally

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
    "displayName": "Prevent client contract sharing externally",
    "description": "Protect client contract confidentiality.",
    "isEnabled": true,
    "mode": "enforce",
    "priority": 1,
    "rules": [
        {
            "id": "rule-62332",
            "name": "Prevent client contract sharing externally",
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