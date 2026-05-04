# ZDI-22-1064: OPC Foundation UA .NET Standard BrowseRequest Missing Authentication Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1064
- **ZDI-CAN:** ZDI-CAN-17371
- **Date:** 2022-08-05
- **CVE:** CVE-2022-33916
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** OPC Foundation
- **Affected Products:** UA .NET Standard
- **Credit:** Uri Katz of Claroty Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1064/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of OPC Foundation UA .NET Standard. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of OPC UA BrowseRequests. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to disclose information in the context of the service.

## Additional Details

OPC Foundation has issued an update to correct this vulnerability. More details can be found at: https://files.opcfoundation.org/SecurityBulletins/OPC%20Foundation%20Security%20Bulletin%20CVE-2022-33916.pdf

## Disclosure Timeline

- 2022-06-07 - Vulnerability reported to vendor
- 2022-08-05 - Coordinated public release of advisory
