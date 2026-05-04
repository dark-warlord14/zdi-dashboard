# ZDI-25-422: Microsoft Azure Machine Learning Environments Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-422
- **ZDI-CAN:** ZDI-CAN-24823
- **Date:** 2025-06-25
- **CVE:** N/A
- **CVSS:** 3.7
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:L
- **Affected Vendors:** Microsoft
- **Affected Products:** Azure
- **Credit:** Nitesh Surana (@_niteshsurana) of Trend Micro Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-422/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Microsoft Azure. Authentication is not required to exploit this vulnerability. The specific flaw exists within Azure Machine Learning Environments. The issue results from predictable Azure Container Registry names. An attacker can leverage this vulnerability to create a denial-of-service condition on the AML workspace.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/acknowledgement/online

## Disclosure Timeline

- 2024-07-12 - Vulnerability reported to vendor
- 2025-06-25 - Coordinated public release of advisory
- 2025-06-25 - Advisory Updated
