# ZDI-20-648: Microsoft SharePoint Shared Forms Incomplete Blacklist Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-648
- **ZDI-CAN:** ZDI-CAN-10124
- **Date:** 2020-05-12
- **CVE:** CVE-2020-1102
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** SharePoint
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-648/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft SharePoint. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of shared forms. It is possible to invoke a shared form in a way that allows arbitrary controls to be instantiated. An attacker can leverage this vulnerability to execute code in the context of the SharePoint web server process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-1102

## Disclosure Timeline

- 2020-01-21 - Vulnerability reported to vendor
- 2020-05-12 - Coordinated public release of advisory
