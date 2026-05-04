# ZDI-16-700: Google Chrome PDFium JPEG Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-700
- **ZDI-CAN:** ZDI-CAN-3655
- **Date:** 2017-08-23
- **CVE:** CVE-2016-10403
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Google
- **Affected Products:** Chrome
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-700/
## Vulnerability Details

This vulnerability allows an attacker to leak sensitive information on vulnerable installations of Google Chrome. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of JPEG images. A specially crafted JPEG image embedded inside a PDF can force Google Chrome to read memory past the end of an allocated object. An attacker can leverage this vulnerability to disclose the contents of adjacent memory.

## Additional Details

Google has issued an update to correct this vulnerability. More details can be found at: https://chromereleases.googleblog.com/2016/05/stable-channel-update_25.html

## Disclosure Timeline

- 2016-04-09 - Vulnerability reported to vendor
- 2017-08-23 - Coordinated public release of advisory
