# ZDI-25-222: (Pwn2Own) Lexmark CX331adwe concatstrings Type Confusion Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-222
- **ZDI-CAN:** ZDI-CAN-25674
- **Date:** 2025-04-09
- **CVE:** CVE-2024-11346
- **CVSS:** 4.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** Lexmark
- **Affected Products:** CX331adwe
- **Credit:** Chris Anastasio @mufinnnnnnn & Fabius Watson
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-222/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to disclose sensitive information on affected installations of Lexmark CX331adwe printers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the concatstrings method. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the device.

## Additional Details

Lexmark has issued an update to correct this vulnerability. More details can be found at: https://support.lexmark.com/content/dam/support/collateral/security-alerts/CVE-2024-11346.pdf

## Disclosure Timeline

- 2024-11-15 - Vulnerability reported to vendor
- 2025-04-09 - Coordinated public release of advisory
- 2025-04-09 - Advisory Updated
