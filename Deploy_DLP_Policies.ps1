# PowerShell Script to Deploy DLP Policies via Microsoft Graph API

# Connect to Graph API (requires appropriate permissions and App Registration)
Connect-MgGraph -Scopes "https://graph.microsoft.com/.default"

# Set the base folder for DLP policies (modify this path if needed)
$baseFolder = "./Policies"

# Loop through each industry folder
$industryFolders = Get-ChildItem -Path $baseFolder -Directory
foreach ($folder in $industryFolders) {
    Write-Host "Processing policies in: $($folder.Name)"
    $policyFiles = Get-ChildItem -Path $folder.FullName -Filter "*.json"
    
    foreach ($file in $policyFiles) {
        Write-Host "Deploying policy: $($file.Name)"
        $policyContent = Get-Content $file.FullName -Raw | ConvertFrom-Json

        # Perform Graph API call
        try {
            Invoke-MgGraphRequest -Method POST -Uri "https://graph.microsoft.com/v1.0/security/dataLossPreventionPolicies" -Body ($policyContent | ConvertTo-Json -Depth 10)
            Write-Host "Successfully deployed: $($file.Name)"
        } catch {
            Write-Error "Failed to deploy: $($file.Name) - Error: $_"
        }
    }
}

# Disconnect from Graph API
Disconnect-MgGraph