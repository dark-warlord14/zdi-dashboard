# ZDI-25-220: (Pwn2Own) Lexmark CX331adwe basic_auth.cgi PATH_TRANSLATED Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-220
- **ZDI-CAN:** ZDI-CAN-25848
- **Date:** 2025-04-09
- **CVE:** N/A
- **CVSS:** 6.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Lexmark
- **Affected Products:** CX331adwe
- **Credit:** nella17 (@nella17tw), working with DEVCORE Internship Program, and DEVCORE Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-220/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Lexmark CX331adwe printers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of the PATH_TRANSLATED parameter provided to the basic_auth.cgi endpoint. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of the pagemaker user.

## Additional Details

Fixed in CXLBL.230.408

## Disclosure Timeline

- 2024-12-12 - Vulnerability reported to vendor
- 2025-04-09 - Coordinated public release of advisory
- 2025-04-09 - Advisory Updated
