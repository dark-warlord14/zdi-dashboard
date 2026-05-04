# ZDI-22-074: Microsoft SharePoint Server-Side Control Improper Input Validation Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-074
- **ZDI-CAN:** ZDI-CAN-14978
- **Date:** 2022-01-14
- **CVE:** CVE-2021-42309
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** SharePoint
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-074/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft SharePoint. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of server-side controls. An unsafe server-side control can be instantiated if it is specified as a child of a permitted control. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-42309

## Disclosure Timeline

- 2021-09-03 - Vulnerability reported to vendor
- 2022-01-14 - Coordinated public release of advisory
