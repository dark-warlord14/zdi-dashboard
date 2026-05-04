# ZDI-23-566: Adobe Substance 3D Painter USD File Parsing Uninitialized Variable Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-566
- **ZDI-CAN:** ZDI-CAN-20369
- **Date:** 2023-05-10
- **CVE:** CVE-2023-29286
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Substance 3D Painter
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-566/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Adobe Substance 3D Painter. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of USD files. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/substance3d_painter/apsb23-29.html

## Disclosure Timeline

- 2023-02-07 - Vulnerability reported to vendor
- 2023-05-10 - Coordinated public release of advisory
