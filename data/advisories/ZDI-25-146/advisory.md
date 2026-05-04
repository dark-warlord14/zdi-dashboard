# ZDI-25-146: (0Day) NI FlexLogger usiReg URI File Parsing Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-146
- **ZDI-CAN:** ZDI-CAN-21805
- **Date:** 2025-03-17
- **CVE:** CVE-2025-2449
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** NI
- **Affected Products:** FlexLogger
- **Credit:** 06fe5fd2bc53027c4a3b7e395af0b850e7b8a044
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-146/
## Vulnerability Details

This vulnerability allows remote attackers to create arbitrary files on affected installations of NI FlexLogger. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of URI files by the usiReg component. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

03/13/24 – ZDI reported the vulnerability to the vendor 03/15/24 - the vendor acknowledged the receipt of the report 12/11/24 - ZDI asked for updates 12/18/24 - the vendor requested an extension until January 2025 01/31/25 - ZDI asked for updates 03/03/25 - ZDI notified the vendor of the intention to publish the case as a 0-day advisory

## Disclosure Timeline

- 2024-03-13 - Vulnerability reported to vendor
- 2025-03-17 - Coordinated public release of advisory
- 2025-03-17 - Advisory Updated
