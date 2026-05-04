# ZDI-22-332: (Pwn2Own) Lexmark MC3224i Web Configuration File Code Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-332
- **ZDI-CAN:** ZDI-CAN-15844
- **Date:** 2022-02-15
- **CVE:** CVE-2021-44734
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Lexmark
- **Affected Products:** MC3224i
- **Credit:** DEVCORE Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-332/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Lexmark MC3224i printers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the HTTP server. The issue results from the lack of proper validation of a user-supplied string before using it to write to a configuration file. An attacker can leverage this vulnerability to execute code in the context of the www-data user.

## Additional Details

Lexmark has issued an update to correct this vulnerability. More details can be found at: https://publications.lexmark.com/publications/security-alerts/CVE-2021-44734.pdf

## Disclosure Timeline

- 2022-01-21 - Vulnerability reported to vendor
- 2022-02-15 - Coordinated public release of advisory
