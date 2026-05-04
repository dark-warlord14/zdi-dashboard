# ZDI-19-813: Microsoft SharePoint Business Data Connectivity Service Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-813
- **ZDI-CAN:** ZDI-CAN-8161
- **Date:** 2019-09-10
- **CVE:** CVE-2019-1296
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** SharePoint
- **Credit:** Markus Wulftange (@mwulftange)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-813/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft SharePoint. Authentication as a high-privileged user is required to exploit this vulnerability. The specific flaw exists within the Business Data Connectivity Service. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the SharePoint application pool identity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1296

## Disclosure Timeline

- 2019-07-03 - Vulnerability reported to vendor
- 2019-09-10 - Coordinated public release of advisory
