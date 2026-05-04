# ZDI-21-587: Adobe After Effects TIF File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-587
- **ZDI-CAN:** ZDI-CAN-13526
- **Date:** 2021-05-13
- **CVE:** CVE-2021-28587
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** After Effects
- **Credit:** Mat Powell (@mrpowell) & Joshua Smith (@kernelsmith) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-587/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Adobe After Effects. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of TIF images. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/after_effects/apsb21-33.html

## Disclosure Timeline

- 2021-03-31 - Vulnerability reported to vendor
- 2021-05-13 - Coordinated public release of advisory
