# ZDI-18-1422: Adobe Acrobat Pro DC EMF Parsing Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1422
- **ZDI-CAN:** ZDI-CAN-6726
- **Date:** 2018-12-17
- **CVE:** CVE-2018-16014
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** GDPR
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1422/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of EMF files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb18-41.html

## Disclosure Timeline

- 2018-09-06 - Vulnerability reported to vendor
- 2018-12-17 - Coordinated public release of advisory
- 2023-06-22 - Advisory Updated
