# ZDI-22-333: (Pwn2Own) Lexmark MC3224i PJL Exposed Dangerous Function Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-333
- **ZDI-CAN:** ZDI-CAN-15820
- **Date:** 2022-02-15
- **CVE:** CVE-2021-44737
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Lexmark
- **Affected Products:** MC3224i
- **Credit:** NCC Group EDG (Alex Plaskett, Cedric Halbronn, Aaron Adams)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-333/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Lexmark MC3224i printers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of PJL commands. The issue results from an exposed danagerous function, which can allow the creation of arbitrary files. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Lexmark has issued an update to correct this vulnerability. More details can be found at: https://publications.lexmark.com/publications/security-alerts/CVE-2021-44737.pdf

## Disclosure Timeline

- 2022-01-21 - Vulnerability reported to vendor
- 2022-02-15 - Coordinated public release of advisory
