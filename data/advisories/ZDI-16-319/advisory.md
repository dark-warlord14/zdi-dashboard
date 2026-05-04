# ZDI-16-319: Adobe Reader DC U3D Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-319
- **ZDI-CAN:** ZDI-CAN-3541
- **Date:** 2016-05-10
- **CVE:** CVE-2016-1071
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-319/
## Vulnerability Details

This vulnerability allows an attacker to leak sensitive information on vulnerable installations of Adobe Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of U3D files. The issue lies in the failure to ensure that user-supplied input is within the bounds of an allocated buffer. An attacker can leverage this vulnerability to disclose the contents of adjacent memory.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb16-14.html

## Disclosure Timeline

- 2016-02-04 - Vulnerability reported to vendor
- 2016-05-10 - Coordinated public release of advisory
