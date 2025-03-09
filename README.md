# Microsoft DLP Graph API Policy Catalog

## Overview

This repository contains **Microsoft Data Loss Prevention (DLP) policy templates** formatted for **Graph API** deployment. The policies are designed to be **industry-specific** and **AI-readiness**, covering a wide range of use cases including healthcare, banking, education, general enterprise, and AI/LLM usage. 

Each policy is organized by industry and includes a **Graph API call sample** for easy deployment into Microsoft Purview / Microsoft Compliance solutions.

## 📂 Repository Structure

```
- Healthcare/
- Banking/
- Education/
- AI/
- General/
- OverlapBuckets/ (multi-industry shared rules)
```

Each folder contains:
- **Individual DLP Policy JSON files** ready for API deployment.
- **Graph API Call Samples (.md)** for easy use in Graph Explorer, Postman, or automation workflows.

## 📜 Policy Naming Convention

Each policy file is named using the following pattern:

```
Policy_<Index>_<Policy_Name>.json
Policy_<Index>_<Policy_Name>_GraphAPI_Call.md
```

Example:
```
Policy_1_Block_PHI_sharing_externally.json
Policy_1_Block_PHI_sharing_externally_GraphAPI_Call.md
```

## 🚀 How to Use

### Step 1: Review and Customize

- Browse the folders to find relevant policies for your industry or use case.
- Review the JSON policy template and accompanying API call markdown file.
- Modify any fields if needed (e.g., recipient emails, thresholds, template IDs).

### Step 2: Deploy via Microsoft Graph API

#### API Endpoint

```
POST https://graph.microsoft.com/v1.0/security/dataLossPreventionPolicies
```

#### Example Request Headers

```
Authorization: Bearer <YOUR_ACCESS_TOKEN>
Content-Type: application/json
```

#### Example Request Body

Use the content of each `.json` file as the request body.

### Step 3: Automate with Scripts (Optional)

You can also automate deployment using PowerShell or GitHub Actions for CI/CD. (Scripts can be added in a future `/scripts/` directory).

## 🏷️ Industry Coverage

| Industry       | Purpose                                                    |
|----------------|------------------------------------------------------------|
| Healthcare     | Protect PHI, PII, and sensitive health records              |
| Banking        | Secure PCI, PII, and financial data                        |
| Education      | Protect student records, FERPA, and institutional data     |
| AI             | Prevent LLM-based data leakage and AI tool misuse          |
| General        | Standard corporate DLP (PII, IP, credentials, contracts)   |
| OverlapBuckets | Policies covering multiple industries (e.g., Healthcare-Banking) |

## ⚙️ Future Enhancements

- [ ] PowerShell / CLI scripts for automated deployment
- [ ] GitHub Actions for pipeline-based DLP policy management
- [ ] YAML / ARM templates for infrastructure as code (IaC) scenarios

## 🧑‍💼 Authors and Contributors
Microsoft Security Services:
Caleb a McDowell - Director

## 📄 License

Private / Internal Use Only (customize based on your sharing policy)
