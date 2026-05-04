# ZDI-17-466: Microsoft Windows PDF Library JPEG2000 Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-466
- **ZDI-CAN:** ZDI-CAN-4481
- **Date:** 2017-07-11
- **CVE:** CVE-2017-0291
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows PDF Library
- **Credit:** Ke Liu (winsonliu) of Tencent's Xuanwu LAB
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-466/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows PDF Library. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of JPEG2000 images. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated object. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-0291

## Disclosure Timeline

- 2017-02-13 - Vulnerability reported to vendor
- 2017-07-11 - Coordinated public release of advisory
