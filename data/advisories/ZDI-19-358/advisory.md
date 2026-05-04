# ZDI-19-358: Microsoft Office Protocol Handler Directory Traversal File Creation Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-358
- **ZDI-CAN:** ZDI-CAN-7707
- **Date:** 2019-04-15
- **CVE:** CVE-2019-0801
- **CVSS:** 4.2
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:L/I:L/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Office
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-358/
## Vulnerability Details

This vulnerability allows remote attackers to create files in arbitrary locations on vulnerable installations of Microsoft Office. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of URL protocol handlers for various types of Office documents. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to create a file in the context of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0801

## Disclosure Timeline

- 2018-12-19 - Vulnerability reported to vendor
- 2019-04-15 - Coordinated public release of advisory
