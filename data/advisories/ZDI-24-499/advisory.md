# ZDI-24-499: (Pwn2Own) TP-Link Omada ER605 PPTP VPN username Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-499
- **ZDI-CAN:** ZDI-CAN-22446
- **Date:** 2024-05-23
- **CVE:** CVE-2024-5227
- **CVSS:** 7.5
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** TP-Link
- **Affected Products:** Omada ER605
- **Credit:** Chris Anastasio @mufinnnnnnn
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-499/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of TP-Link Omada ER605 routers. Authentication is not required to exploit this vulnerability. However, devices are only vulnerable if configured to use a PPTP VPN with LDAP authentication. The specific flaw exists within the handling of the username parameter provided to the /usr/bin/pppd endpoint. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Fixed in firmware ER605 (UN) _V2_2. 2.4 Build 20240119 https://www.tp-link.com/en/support/download/er605/#Firmware

## Disclosure Timeline

- 2023-11-09 - Vulnerability reported to vendor
- 2024-05-23 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
