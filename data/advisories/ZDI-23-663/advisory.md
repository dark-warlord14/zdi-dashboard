# ZDI-23-663: (Pwn2Own) Lexmark MC3224i pagemaker NAME Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-663
- **ZDI-CAN:** ZDI-CAN-19859
- **Date:** 2023-05-17
- **CVE:** CVE-2023-26063
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Lexmark
- **Affected Products:** MC3224i
- **Credit:** NCC Group EDG (@alexjplaskett @saidelike @FidgetingBits @_mccaulay)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-663/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Lexmark MC3224i printers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the pagemaker service. When parsing the NAME element, the process does not properly validate user-supplied data, which can result in a type confusion condition. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Lexmark has issued an update to correct this vulnerability. More details can be found at: https://publications.lexmark.com/publications/security-alerts/CVE-2023-26063.pdf

## Disclosure Timeline

- 2022-12-28 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory
