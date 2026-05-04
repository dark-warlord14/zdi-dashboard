# ZDI-21-830: Microsoft SharePoint Missing Check of Message Integrity Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-830
- **ZDI-CAN:** ZDI-CAN-13682
- **Date:** 2021-07-19
- **CVE:** CVE-2021-34519
- **CVSS:** 3.5
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:R/S:U/C:N/I:L/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** SharePoint
- **Credit:** mr_me
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-830/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to tamper with update data on affected installations of Microsoft SharePoint. User interaction is required to exploit this vulnerability. The specific flaw exists within the handling of SharePoint Help updates. The issue results from a missing integrity check on update downloads. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the service account.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/en-us/vulnerability/CVE-2021-34519

## Disclosure Timeline

- 2021-05-07 - Vulnerability reported to vendor
- 2021-07-19 - Coordinated public release of advisory
