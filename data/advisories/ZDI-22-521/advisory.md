# ZDI-22-521: (Pwn2Own) NETGEAR R6700v3 Missing Authentication for Critical Function Arbitrary File Upload Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-521
- **ZDI-CAN:** ZDI-CAN-15782
- **Date:** 2022-03-23
- **CVE:** N/A
- **CVSS:** 3.1
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:N/I:L/A:N
- **Affected Vendors:** NETGEAR
- **Affected Products:** R6700v3
- **Credit:** Flashback Team: Pedro Ribeiro (@pedrib1337) && Radek Domanski (@RabbitPro)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-521/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to upload arbitrary files on affected installations of NETGEAR R6700v3 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Circle Parental Control feature, which listens on TCP ports 4444 and 4567 by default. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000064724/Security-Advisory-for-Security-Misconfiguration-on-Some-Routers-and-Orbi-WiFi-Systems-PSV-2021-0330

## Disclosure Timeline

- 2022-01-07 - Vulnerability reported to vendor
- 2022-03-23 - Coordinated public release of advisory
