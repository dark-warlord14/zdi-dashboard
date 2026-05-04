# ZDI-22-328: (Pwn2Own) Lexmark MC3224i PostScript Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-328
- **ZDI-CAN:** ZDI-CAN-15924
- **Date:** 2022-02-15
- **CVE:** CVE-2021-44738
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Lexmark
- **Affected Products:** MC3224i
- **Credit:** Christopher Anastasio @mufinnnnnnn
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-328/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Lexmark MC3224i printers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the parsing of PostScript data. Crafted PostScript data can trigger a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Lexmark has issued an update to correct this vulnerability. More details can be found at: https://publications.lexmark.com/publications/security-alerts/CVE-2021-44738.pdf

## Disclosure Timeline

- 2022-01-26 - Vulnerability reported to vendor
- 2022-02-15 - Coordinated public release of advisory
