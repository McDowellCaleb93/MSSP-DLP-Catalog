### Graph API Call Sample for Monitor Student Records internally

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
    "displayName": "Monitor Student Records internally",
    "description": "Detect improper access to student data",
    "isEnabled": true,
    "mode": "test",
    "priority": 1,
    "rules": [
        {
            "id": "rule-40640",
            "name": "Monitor Student Records internally",
            "actions": [
                {
                    "type": "audit"
                }
            ],
            "conditions": {
                "contentContainsSensitiveInformation": [
                    {
                        "sensitiveTypeId": "education-student-record-sit",
                        "minCount": 1,
                        "confidenceLevel": "high"
                    }
                ],
                "contentContainsAnyOfWords": []
            },
            "locations": [
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
                    "compliance@company.com"
                ]
            }
        }
    ]
}
```