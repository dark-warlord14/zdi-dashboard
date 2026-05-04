# ZDI-21-084: Tencent WeChat WXAM Decoder Out-Of-Bounds Access Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-084
- **ZDI-CAN:** ZDI-CAN-11580
- **Date:** 2021-01-22
- **CVE:** CVE-2020-27874
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Tencent
- **Affected Products:** WeChat
- **Credit:** Wen guang Jiao
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-084/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Tencent WeChat. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the WXAM Decoder. The issue results from the lack of proper validation of user-supplied data, which can result in a memory access past the end of an allocated object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed in version7.0.19

## Disclosure Timeline

- 2020-09-08 - Vulnerability reported to vendor
- 2021-01-22 - Coordinated public release of advisory
