# ZDI-20-334: (Pwn2Own) TP-Link Archer A7 tdpServer Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-334
- **ZDI-CAN:** ZDI-CAN-9650
- **Date:** 2020-03-25
- **CVE:** CVE-2020-10882
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** TP-Link
- **Affected Products:** Archer A7
- **Credit:** Pedro Ribeiro and Radek Domanski of Team Flashback
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-334/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of TP-Link Archer A7 AC1750 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the tdpServer service, which listens on UDP port 20002 by default. When parsing the slave_mac parameter, the process does not properly validate a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of the root user.

## Additional Details

Fixed in version A7(US)_V5_200220

## Disclosure Timeline

- 2019-11-19 - Vulnerability reported to vendor
- 2020-03-25 - Coordinated public release of advisory
