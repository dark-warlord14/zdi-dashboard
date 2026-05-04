# ZDI-15-475: Adobe Acrobat Pro DC Color Object Address Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-475
- **ZDI-CAN:** ZDI-CAN-3036
- **Date:** 2015-10-13
- **CVE:** CVE-2015-6697
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** AbdulAziz Hariri - HP Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-475/
## Vulnerability Details

This vulnerability allows remote attackers to gain information about the layout of memory on vulnerable installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of color objects in light objects. The RGB values returned from a newly created light object can disclose the heap address of a color object. An attacker can use this information in conjunction with other vulnerabilities to execute code in the context of the process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb15-24.html

## Disclosure Timeline

- 2015-07-02 - Vulnerability reported to vendor
- 2015-10-13 - Coordinated public release of advisory
