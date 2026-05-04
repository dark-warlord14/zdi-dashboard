# ZDI-25-652: (Pwn2Own) Microsoft SharePoint ToolPane Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-652
- **ZDI-CAN:** ZDI-CAN-27790
- **Date:** 2025-07-25
- **CVE:** CVE-2025-53771
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** SharePoint
- **Credit:** Viettel Cyber Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-652/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Microsoft SharePoint. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ToolPane endpoint. The application does not adequately restrict access to a protected API. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-53771

## Disclosure Timeline

- 2025-07-24 - Vulnerability reported to vendor
- 2025-07-25 - Coordinated public release of advisory
- 2025-07-25 - Advisory Updated
