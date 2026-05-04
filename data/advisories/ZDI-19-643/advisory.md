# ZDI-19-643: Microsoft Office Excel Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-643
- **ZDI-CAN:** ZDI-CAN-7749
- **Date:** 2019-07-10
- **CVE:** CVE-2019-1110
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Excel
- **Credit:** yingxinlei and liujialing
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-643/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable instances of Microsoft Office Excel. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of note nodes within xls files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1110

## Disclosure Timeline

- 2019-01-25 - Vulnerability reported to vendor
- 2019-07-10 - Coordinated public release of advisory
