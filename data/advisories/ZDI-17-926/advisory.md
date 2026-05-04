# ZDI-17-926: Adobe Photoshop JPEG2000 Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-926
- **ZDI-CAN:** ZDI-CAN-4891
- **Date:** 2017-11-20
- **CVE:** CVE-2017-11304
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Photoshop
- **Credit:** TrendyTofu - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-926/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Adobe Photoshop. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of JPEG2000 images. When parsing a crafted image, the process does not properly validate the existence of an object prior to performing operations on the object. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/photoshop/apsb17-34.html

## Disclosure Timeline

- 2017-07-06 - Vulnerability reported to vendor
- 2017-11-20 - Coordinated public release of advisory
