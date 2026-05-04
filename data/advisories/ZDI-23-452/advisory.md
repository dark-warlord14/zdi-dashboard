# ZDI-23-452: (Pwn2Own) TP-Link AX1800 hotplugd Firewall Rule Race Condition Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-452
- **ZDI-CAN:** ZDI-CAN-19664
- **Date:** 2023-04-24
- **CVE:** CVE-2023-27359
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** TP-Link
- **Affected Products:** AX1800
- **Credit:** Pham Nguyen Ngoc Bien & Dang Minh Tri from Qrious Secure
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-452/
## Vulnerability Details

This vulnerability allows remote attackers to gain access to LAN-side services on affected installations of TP-Link Archer AX21 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the hotplugd daemon. The issue results from firewall rule handling that allows an attacker access to resources that should be available to the LAN interface only. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the root user.

## Additional Details

TP-Link has issued an update to correct this vulnerability. More details can be found at: https://www.tp-link.com/us/support/download/archer-ax21/v3/#Firmware

## Disclosure Timeline

- 2022-12-28 - Vulnerability reported to vendor
- 2023-04-24 - Coordinated public release of advisory
