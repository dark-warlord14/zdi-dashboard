# ZDI-23-1396: Visualware MyConnection Server doPostUploadfiles Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1396
- **ZDI-CAN:** ZDI-CAN-21612
- **Date:** 2023-09-08
- **CVE:** CVE-2023-42033
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Visualware
- **Affected Products:** MyConnection Server
- **Credit:** 06fe5fd2bc53027c4a3b7e395af0b850e7b8a044
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1396/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Visualware MyConnection Server. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the doPostUploadfiles method. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Visualware has issued an update to correct this vulnerability. More details can be found at: https://myconnectionserver.visualware.com/support/security-advisories

## Disclosure Timeline

- 2023-07-28 - Vulnerability reported to vendor
- 2023-09-08 - Coordinated public release of advisory
