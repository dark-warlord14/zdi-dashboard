# ZDI-22-986: Adobe Photoshop U3D File Parsing Uninitialized Variable Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-986
- **ZDI-CAN:** ZDI-CAN-17002
- **Date:** 2022-07-13
- **CVE:** CVE-2022-34244
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Photoshop
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-986/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Adobe Photoshop. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of U3D files. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/photoshop/apsb22-35.html

## Disclosure Timeline

- 2022-03-30 - Vulnerability reported to vendor
- 2022-07-13 - Coordinated public release of advisory
