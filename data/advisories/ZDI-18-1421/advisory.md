# ZDI-18-1421: Adobe Acrobat Pro DC EMF Parsing Untrusted Pointer Dereference Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1421
- **ZDI-CAN:** ZDI-CAN-6720
- **Date:** 2018-12-17
- **CVE:** CVE-2018-12845
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** GDPR
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1421/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of EMF files. The issue results from the lack of proper validation of a user-supplied value prior to dereferencing it as a pointer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb18-30.html

## Disclosure Timeline

- 2018-09-06 - Vulnerability reported to vendor
- 2018-12-17 - Coordinated public release of advisory
- 2023-06-22 - Advisory Updated
