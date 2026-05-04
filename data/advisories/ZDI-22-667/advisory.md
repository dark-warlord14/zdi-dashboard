# ZDI-22-667: Adobe Acrobat Reader DC Annotation Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-667
- **ZDI-CAN:** ZDI-CAN-16864
- **Date:** 2022-04-28
- **CVE:** CVE-2022-28250
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-667/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information code on affected installations of Adobe Acrobat Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of Annotation objects. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb22-16.html

## Disclosure Timeline

- 2022-03-11 - Vulnerability reported to vendor
- 2022-04-28 - Coordinated public release of advisory
