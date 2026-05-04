# ZDI-18-1371: Adobe Acrobat Pro DC Onix ReadBTreeT::FindKeyInInteriorPage Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1371
- **ZDI-CAN:** ZDI-CAN-6897
- **Date:** 2018-12-12
- **CVE:** CVE-2018-16045
- **CVSS:** 5.2
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:C/C:L/I:L/A:L
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** Sebastian Apelt (@bitshifter123)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1371/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of arguments passed to the ReadBTreeT::FindKeyInInteriorPage method. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated object. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb18-41.html

## Disclosure Timeline

- 2018-07-22 - Vulnerability reported to vendor
- 2018-12-12 - Coordinated public release of advisory
