# ZDI-23-546: Microsoft SharePoint Chart Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-546
- **ZDI-CAN:** ZDI-CAN-16664
- **Date:** 2023-05-04
- **CVE:** CVE-2022-29108
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** SharePoint
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-546/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft SharePoint Server. Authentication is required to exploit this vulnerability. The specific flaw exists within the processing of charts. Tampering with client-side data can trigger the deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the SharePoint web server process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-29108

## Disclosure Timeline

- 2022-03-04 - Vulnerability reported to vendor
- 2023-05-04 - Coordinated public release of advisory
