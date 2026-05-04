# ZDI-18-174: Adobe Acrobat Pro DC Bookmark Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-174
- **ZDI-CAN:** ZDI-CAN-5577
- **Date:** 2018-02-21
- **CVE:** CVE-2018-4911
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-174/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of Bookmark objects. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb18-02.html

## Disclosure Timeline

- 2018-01-12 - Vulnerability reported to vendor
- 2018-02-21 - Coordinated public release of advisory
- 2018-02-21 - Advisory Updated
