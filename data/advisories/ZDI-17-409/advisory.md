# ZDI-17-409: Microsoft Windows OTL Font Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-409
- **ZDI-CAN:** ZDI-CAN-4701
- **Date:** 2017-06-13
- **CVE:** CVE-2017-0285
- **CVSS:** 2.6
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Ke Liu of Tencent's Xuanwu LAB
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-409/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of OpenType Layout (OTL) data in font files. The issue results from the lack of proper validation of user-supplied data, which can result in a read outside an allocated object. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-0285

## Disclosure Timeline

- 2017-05-04 - Vulnerability reported to vendor
- 2017-06-13 - Coordinated public release of advisory
