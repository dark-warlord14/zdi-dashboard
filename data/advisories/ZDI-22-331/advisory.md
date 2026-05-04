# ZDI-22-331: (Pwn2Own) Lexmark MC3224i Unprotected API Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-331
- **ZDI-CAN:** ZDI-CAN-15800
- **Date:** 2022-02-15
- **CVE:** CVE-2021-44736
- **CVSS:** 9.6
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:C/C:L/I:H/A:H
- **Affected Vendors:** Lexmark
- **Affected Products:** MC3224i
- **Credit:** David BERARD (@_p0ly_), Vincent FARGUES (@Karion_), Thomas IMBERT (@masthoon), from @Synacktiv
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-331/
## Vulnerability Details

This vulnerability allows remote attackers to remove authentication on affected installations of Lexmark MC3224i printers. Authentication is not required to exploit this vulnerability. The specific flaw exists within URL handling. The issue results from the lack of proper restriction to a URL. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Lexmark has issued an update to correct this vulnerability. More details can be found at: https://publications.lexmark.com/publications/security-alerts/CVE-2021-44736.pdf

## Disclosure Timeline

- 2021-11-08 - Vulnerability reported to vendor
- 2022-02-15 - Coordinated public release of advisory
