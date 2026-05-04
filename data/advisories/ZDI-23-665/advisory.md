# ZDI-23-665: (Pwn2Own) Lexmark MC3224i putinterval Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-665
- **ZDI-CAN:** ZDI-CAN-19822
- **Date:** 2023-05-17
- **CVE:** CVE-2023-26065
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Lexmark
- **Affected Products:** MC3224i
- **Credit:** Chris Anastasio (@mufinnnnnnn)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-665/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Lexmark MC3224i printers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the PostScript putinterval command. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to execute code in the context of the device.

## Additional Details

Lexmark has issued an update to correct this vulnerability. More details can be found at: https://publications.lexmark.com/publications/security-alerts/CVE-2023-26065.pdf

## Disclosure Timeline

- 2023-01-26 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory
