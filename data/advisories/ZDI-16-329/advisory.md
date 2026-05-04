# ZDI-16-329: Adobe Reader DC JPEG2000 Out-of-Bounds Read Information DIsclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-329
- **ZDI-CAN:** ZDI-CAN-3633
- **Date:** 2016-05-10
- **CVE:** CVE-2016-1095
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-329/
## Vulnerability Details

This vulnerability allows an attacker to leak sensitive information on vulnerable installations of Adobe Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of JPEG2000 files. The issue lies in the failure to validate the value of the vsep of the last component. An attacker can leverage this vulnerability to disclose the contents of adjacent memory.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb16-14.html

## Disclosure Timeline

- 2016-03-29 - Vulnerability reported to vendor
- 2016-05-10 - Coordinated public release of advisory
