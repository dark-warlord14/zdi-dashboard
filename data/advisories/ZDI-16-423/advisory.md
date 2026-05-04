# ZDI-16-423: Adobe Reader DC JPEG2000 Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-423
- **ZDI-CAN:** ZDI-CAN-3656
- **Date:** 2016-07-12
- **CVE:** CVE-2016-4191
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-423/
## Vulnerability Details

This vulnerability allows an attacker to leak sensitive information on vulnerable installations of Adobe Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of JPEG2000 files. The issue lies in the failure to validate multiple fields in the JPEG2000 file structure. An attacker can leverage this vulnerability to disclose the contents of adjacent memory.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb16-26.html

## Disclosure Timeline

- 2016-04-07 - Vulnerability reported to vendor
- 2016-07-12 - Coordinated public release of advisory
