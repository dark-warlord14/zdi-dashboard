# ZDI-20-694: Microsoft SharePoint Server Web Part Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-694
- **ZDI-CAN:** ZDI-CAN-10589
- **Date:** 2020-06-09
- **CVE:** CVE-2020-1181
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** SharePoint
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-694/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft SharePoint Server. Authentication is required to exploit this vulnerability. The specific flaw exists within the handling of Web Parts. When creating a SharePoint page, an attacker can upload XML containing an arbitrary Web Part definition. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-1181

## Disclosure Timeline

- 2020-03-03 - Vulnerability reported to vendor
- 2020-06-09 - Coordinated public release of advisory
