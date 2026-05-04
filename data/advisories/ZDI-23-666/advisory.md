# ZDI-23-666: (Pwn2Own) Lexmark MC3224i pagemark Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-666
- **ZDI-CAN:** ZDI-CAN-19685
- **Date:** 2023-05-17
- **CVE:** CVE-2023-26066
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Lexmark
- **Affected Products:** MC3224i
- **Credit:** NCC Group EDG (@alexjplaskett @saidelike @FidgetingBits @_mccaulay)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-666/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Lexmark MC3224i printers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the pagemark service. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated data structure. An attacker can leverage this vulnerability to execute arbitrary code in the context of the admin user.

## Additional Details

Lexmark has issued an update to correct this vulnerability. More details can be found at: https://publications.lexmark.com/publications/security-alerts/CVE-2023-26066.pdf

## Disclosure Timeline

- 2023-01-24 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory
