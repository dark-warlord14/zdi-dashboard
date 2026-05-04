# ZDI-18-642: Adobe Acrobat Pro DC WebLink rect Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-642
- **ZDI-CAN:** ZDI-CAN-6308
- **Date:** 2018-07-13
- **CVE:** CVE-2018-12797
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-642/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the rect attribute in link objects. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb18-21.html

## Disclosure Timeline

- 2018-06-11 - Vulnerability reported to vendor
- 2018-07-13 - Coordinated public release of advisory
- 2018-07-13 - Advisory Updated
