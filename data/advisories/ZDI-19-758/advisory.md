# ZDI-19-758: Adobe Acrobat Pro DC AcroForm strokeColor Property Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-758
- **ZDI-CAN:** ZDI-CAN-8797
- **Date:** 2019-08-19
- **CVE:** CVE-2019-8056
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-758/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the strokeColor property of Field objects in the AcroForm plugin. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb19-41.html

## Disclosure Timeline

- 2019-06-27 - Vulnerability reported to vendor
- 2019-08-19 - Coordinated public release of advisory
