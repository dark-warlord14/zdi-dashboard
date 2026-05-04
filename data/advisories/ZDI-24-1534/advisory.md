# ZDI-24-1534: Microsoft SharePoint Server FindSpecific Unsafe Reflection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1534
- **ZDI-CAN:** ZDI-CAN-24221
- **Date:** 2024-11-20
- **CVE:** CVE-2024-38024
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** SharePoint
- **Credit:** Guy Lederfein of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1534/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft SharePoint Server. Authentication is required to exploit this vulnerability. The specific flaw exists within the implementation of the FindSpecific method. The process does not properly restrict a user-supplied argument before using it to create an instance of an object. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-38024

## Disclosure Timeline

- 2024-05-28 - Vulnerability reported to vendor
- 2024-11-20 - Coordinated public release of advisory
- 2024-11-20 - Advisory Updated
