# ZDI-24-073: Paessler PRTG Network Monitor Cross-Site Scripting Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-073
- **ZDI-CAN:** ZDI-CAN-21182
- **Date:** 2024-01-15
- **CVE:** CVE-2023-51630
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Paessler
- **Affected Products:** PRTG Network Monitor
- **Credit:** n1nj4sec
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-073/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Paessler PRTG Network Monitor. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the web console. The issue results from the lack of proper validation of user-supplied data, which can lead to the injection of an arbitrary script. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Fixed in PRTG version 24.1.90.1306 https://www.paessler.com/prtg/history/stable

## Disclosure Timeline

- 2023-06-15 - Vulnerability reported to vendor
- 2024-01-15 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
