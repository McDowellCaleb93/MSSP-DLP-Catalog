### Graph API Call Sample for Prevent sensitive health data sharing

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
    "displayName": "Prevent sensitive health data sharing",
    "description": "Stop accidental PHI/health data sharing.",
    "isEnabled": true,
    "mode": "enforce",
    "priority": 1,
    "rules": [
        {
            "id": "rule-33933",
            "name": "Prevent sensitive health data sharing",
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