# ZDI-16-565: Adobe Reader DC JPEG2000 Out-Of-Bounds Read Information DIsclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-565
- **ZDI-CAN:** ZDI-CAN-3740
- **Date:** 2016-10-11
- **CVE:** CVE-2016-6941
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-565/
## Vulnerability Details

This vulnerability allows an attacker to leak sensitive information on vulnerable installations of Adobe Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of JPEG2000 images. A malformed JPEG2000 image embedded inside a PDF can force Adobe Reader DC to read memory past the end of an allocated object. An attacker can leverage this vulnerability to disclose the contents of adjacent memory.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb16-33.html

## Disclosure Timeline

- 2016-05-05 - Vulnerability reported to vendor
- 2016-10-11 - Coordinated public release of advisory
