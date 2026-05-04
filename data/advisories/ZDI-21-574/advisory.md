# ZDI-21-574: Microsoft SharePoint Server-Side Control Interpretation Conflict Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-574
- **ZDI-CAN:** ZDI-CAN-12949
- **Date:** 2021-05-13
- **CVE:** CVE-2021-28474
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** SharePoint
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-574/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft SharePoint. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of server-side controls. By specifying a control using a non-canonical string, an unsafe server-side control can be instantiated. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-28474

## Disclosure Timeline

- 2021-02-08 - Vulnerability reported to vendor
- 2021-05-13 - Coordinated public release of advisory
