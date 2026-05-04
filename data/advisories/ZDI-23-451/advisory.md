# ZDI-23-451: (Pwn2Own) TP-Link Archer AX21 merge_country_config Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-451
- **ZDI-CAN:** ZDI-CAN-19557
- **Date:** 2023-04-24
- **CVE:** CVE-2023-1389
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** TP-Link
- **Affected Products:** Archer AX21
- **Credit:** rskvp93, Q5Ca, and hoangnx99 from VcsLab of Viettel Cyber Security and Pham Nguyen Ngoc Bien & Dang Minh Tri from Qrious Secure
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-451/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of TP-Link Archer AX21 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the merge_country_config function. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute arbitrary code in the context of root.

## Additional Details

TP-Link has issued an update to correct this vulnerability. More details can be found at: https://www.tp-link.com/us/support/download/archer-ax21/v3/#Firmware

## Disclosure Timeline

- 2023-01-25 - Vulnerability reported to vendor
- 2023-04-24 - Coordinated public release of advisory
