# ZDI-18-682: Adobe Acrobat Pro DC XFA Template Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-682
- **ZDI-CAN:** ZDI-CAN-6282
- **Date:** 2018-07-16
- **CVE:** CVE-2018-12794
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** Sebastian Apelt siberas
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-682/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of XFA Template objects. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb18-21.html

## Disclosure Timeline

- 2018-06-11 - Vulnerability reported to vendor
- 2018-07-16 - Coordinated public release of advisory
- 2018-07-16 - Advisory Updated
