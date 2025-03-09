### Graph API Call Sample for Monitor financial forecasts sharing

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
    "displayName": "Monitor financial forecasts sharing",
    "description": "Audit sharing of projections and forecasts.",
    "isEnabled": true,
    "mode": "test",
    "priority": 1,
    "rules": [
        {
            "id": "rule-52762",
            "name": "Monitor financial forecasts sharing",
            "actions": [
                {
                    "type": "audit"
                }
            ],
            "conditions": {
                "contentContainsSensitiveInformation": [
                    {
                        "sensitiveTypeId": "general-financial-data-sit",
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