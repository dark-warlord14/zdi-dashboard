# ZDI-24-1128: Samsung MagicINFO 9 Server getFileFromMultipartFile Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1128
- **ZDI-CAN:** ZDI-CAN-23326
- **Date:** 2024-12-09
- **CVE:** CVE-2024-7399
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Samsung
- **Affected Products:** MagicINFO 9 Server
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1128/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Samsung MagicINFO Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the getFileFromMultipartFile method. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Samsung has issued an update to correct this vulnerability. More details can be found at: https://security.samsungtv.com/securityUpdates

## Disclosure Timeline

- 2024-03-08 - Vulnerability reported to vendor
- 2024-12-09 - Coordinated public release of advisory
- 2025-03-05 - Advisory Updated
