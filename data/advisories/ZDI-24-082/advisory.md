# ZDI-24-082: (Pwn2Own) Lexmark CX331adwe PDF File Parsing Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-082
- **ZDI-CAN:** ZDI-CAN-22443
- **Date:** 2024-01-31
- **CVE:** CVE-2023-50735
- **CVSS:** 7.5
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Lexmark
- **Affected Products:** CX331adwe
- **Credit:** Team PHPHooligans
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-082/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Lexmark CX331adwe printers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the parsing of PDF files. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code in the context of the pagemaker user.

## Additional Details

Lexmark has issued an update to correct this vulnerability. More details can be found at: https://www.lexmark.com/en_us/solutions/security/lexmark-security-advisories.html

## Disclosure Timeline

- 2023-11-09 - Vulnerability reported to vendor
- 2024-01-31 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
