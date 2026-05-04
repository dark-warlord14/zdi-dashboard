# ZDI-24-503: (Pwn2Own) TP-Link Omada ER605 Reliance on Security Through Obscurity Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-503
- **ZDI-CAN:** ZDI-CAN-22439
- **Date:** 2024-05-23
- **CVE:** CVE-2024-5244
- **CVSS:** 5.0
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** TP-Link
- **Affected Products:** Omada ER605
- **Credit:** Claroty Research - Team82 - Uri Katz, Noam Moshe, Tomer Goldschmidt, Sharon Brizinov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-503/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to access or spoof DDNS messages on affected installations of TP-Link Omada ER605 routers. Authentication is not required to exploit this vulnerability. However, devices are vulnerable only if configured to use the Comexe DDNS service. The specific flaw exists within the cmxddnsd executable. The issue results from reliance on obscurity to secure network data. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

Fixed in firmware ER605 (UN) _V2_2. 2.4 Build 20240119 https://www.tp-link.com/en/support/download/er605/#Firmware

## Disclosure Timeline

- 2023-11-15 - Vulnerability reported to vendor
- 2024-05-23 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
