# ZDI-24-081: (Pwn2Own) Lexmark CX331adwe make42charstring Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-081
- **ZDI-CAN:** ZDI-CAN-22380
- **Date:** 2024-01-31
- **CVE:** CVE-2023-50734
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Lexmark
- **Affected Products:** CX331adwe
- **Credit:** @vcslab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-081/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Lexmark CX331adwe printers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the make42charstring method. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Lexmark has issued an update to correct this vulnerability. More details can be found at: https://www.lexmark.com/en_us/solutions/security/lexmark-security-advisories.html

## Disclosure Timeline

- 2023-11-09 - Vulnerability reported to vendor
- 2024-01-31 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
