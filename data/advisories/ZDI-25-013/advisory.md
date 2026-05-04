# ZDI-25-013: SonicWALL NSv SSH Management Server-Side Request Forgery Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-013
- **ZDI-CAN:** ZDI-CAN-24820
- **Date:** 2025-01-09
- **CVE:** CVE-2024-53705
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N
- **Affected Vendors:** SonicWALL
- **Affected Products:** NSv
- **Credit:** Daan Keuper, Thijs Alkemade and Khaled Nassar of Computest Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-013/
## Vulnerability Details

This vulnerability allows remote attackers to initiate arbitrary server-side requests on affected installations of SonicWALL NSv. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the SSH Management functionality. The issue results from the lack of proper validation of the length of user-supplied IP addresses and ports. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

SonicWALL has issued an update to correct this vulnerability. More details can be found at: https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2025-0003

## Disclosure Timeline

- 2024-11-05 - Vulnerability reported to vendor
- 2025-01-09 - Coordinated public release of advisory
- 2025-01-09 - Advisory Updated
