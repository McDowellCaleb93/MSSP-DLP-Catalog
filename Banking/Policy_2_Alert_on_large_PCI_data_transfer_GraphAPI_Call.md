### Graph API Call Sample for Alert on large PCI data transfer

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
    "displayName": "Alert on large PCI data transfer",
    "description": "Detect bulk PCI data movements",
    "isEnabled": true,
    "mode": "test",
    "priority": 1,
    "rules": [
        {
            "id": "rule-76771",
            "name": "Alert on large PCI data transfer",
            "actions": [
                {
                    "type": "audit"
                }
            ],
            "conditions": {
                "contentContainsSensitiveInformation": [
                    {
                        "sensitiveTypeId": "banking-pci-sit",
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