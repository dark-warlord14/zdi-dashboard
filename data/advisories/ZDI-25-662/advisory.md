# ZDI-25-662: Samsung MagicINFO 9 Server ResponseUploadActivity Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-662
- **ZDI-CAN:** ZDI-CAN-25955
- **Date:** 2025-07-28
- **CVE:** CVE-2025-54446
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Samsung
- **Affected Products:** MagicINFO 9 Server
- **Credit:** 06fe5fd2bc53027c4a3b7e395af0b850e7b8a044
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-662/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Samsung MagicINFO 9 Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ResponseUploadActivity class. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Samsung has issued an update to correct this vulnerability. More details can be found at: https://security.samsungtv.com/securityUpdates

## Disclosure Timeline

- 2025-03-06 - Vulnerability reported to vendor
- 2025-07-28 - Coordinated public release of advisory
- 2025-07-28 - Advisory Updated
