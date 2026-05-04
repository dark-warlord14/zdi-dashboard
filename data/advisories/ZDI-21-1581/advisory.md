# ZDI-21-1581: Adobe Photoshop Lightroom TIF File Parsing Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1581
- **ZDI-CAN:** ZDI-CAN-15242
- **Date:** 2021-12-21
- **CVE:** CVE-2021-43753
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Photoshop Lightroom
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1581/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of of Adobe Photoshop Lightroom. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of TIF images. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/lightroom/apsb21-119.html

## Disclosure Timeline

- 2021-09-15 - Vulnerability reported to vendor
- 2021-12-21 - Coordinated public release of advisory
