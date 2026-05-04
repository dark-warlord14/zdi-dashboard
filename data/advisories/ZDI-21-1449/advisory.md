# ZDI-21-1449: Tencent WeChat WXAM Decoder Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1449
- **ZDI-CAN:** ZDI-CAN-13624
- **Date:** 2021-12-07
- **CVE:** N/A
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Tencent
- **Affected Products:** WeChat
- **Credit:** Lucas Leong (@_wmliang_) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1449/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Tencent WeChat. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the WXAM decoder. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Fixed in version 8.0.10

## Disclosure Timeline

- 2021-04-14 - Vulnerability reported to vendor
- 2021-12-07 - Coordinated public release of advisory
