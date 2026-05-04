# ZDI-21-1144: Microsoft Project MPT File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1144
- **ZDI-CAN:** ZDI-CAN-14518
- **Date:** 2021-10-06
- **CVE:** N/A
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Project
- **Credit:** Tran Van Khang - khangkito (VinCSS)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1144/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Microsoft Project. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of MPT files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this vulnerability to disclose information in the context of the current process.

## Additional Details

fixed in version 16.0.14228.20000

## Disclosure Timeline

- 2021-07-30 - Vulnerability reported to vendor
- 2021-10-06 - Coordinated public release of advisory
