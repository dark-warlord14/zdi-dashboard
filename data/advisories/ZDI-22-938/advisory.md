# ZDI-22-938: Tencent WeChat WXAM Decoder Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-938
- **ZDI-CAN:** ZDI-CAN-16211
- **Date:** 2022-06-30
- **CVE:** N/A
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Tencent
- **Affected Products:** WeChat
- **Credit:** Lucas Leong (@_wmliang_) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-938/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Tencent WeChat. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the WXAM decoder. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in version 8.0.22

## Disclosure Timeline

- 2021-12-30 - Vulnerability reported to vendor
- 2022-06-30 - Coordinated public release of advisory
