# ZDI-21-973: (Pwn2Own) Zoom Client GIPHY URL Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-973
- **ZDI-CAN:** ZDI-CAN-13617
- **Date:** 2021-08-17
- **CVE:** N/A
- **CVSS:** 5.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:L/A:N
- **Affected Vendors:** Zoom
- **Affected Products:** Client
- **Credit:** Daan Keuper and Thijs Alkemade from Computest
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-973/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Zoom Clients. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of GIPHY messages. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current user.

## Additional Details

Zoom has issued an update to correct this vulnerability. More details can be found at: https://explore.zoom.us/en/trust/security/security-bulletin/

## Disclosure Timeline

- 2021-04-07 - Vulnerability reported to vendor
- 2021-08-17 - Coordinated public release of advisory
