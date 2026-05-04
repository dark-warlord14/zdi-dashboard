# ZDI-19-812: Microsoft SharePoint Business Data Connectivity Service Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-812
- **ZDI-CAN:** ZDI-CAN-8159
- **Date:** 2019-09-10
- **CVE:** CVE-2019-1257
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** SharePoint
- **Credit:** Markus Wulftange (@mwulftange)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-812/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft SharePoint. Authentication is required to exploit this vulnerability. The specific flaw exists within the Business Data Connectivity Service. A crafted request can trigger the deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the SharePoint application pool identity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1257

## Disclosure Timeline

- 2019-07-03 - Vulnerability reported to vendor
- 2019-09-10 - Coordinated public release of advisory
