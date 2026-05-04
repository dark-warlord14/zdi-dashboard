# ZDI-21-217: Tencent WeChat WXAM Decoder Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-217
- **ZDI-CAN:** ZDI-CAN-11907
- **Date:** 2021-02-24
- **CVE:** CVE-2021-27247
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N
- **Affected Vendors:** Tencent
- **Affected Products:** WeChat
- **Credit:** Wen guang Jiao
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-217/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Tencent WeChat. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the WXAM decoder. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Fixed in version 3.1.0

## Disclosure Timeline

- 2020-09-25 - Vulnerability reported to vendor
- 2021-02-24 - Coordinated public release of advisory
