# ZDI-16-243: Google Chrome Pdfium JPEG2000 Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-243
- **ZDI-CAN:** ZDI-CAN-3594
- **Date:** 2016-04-15
- **CVE:** CVE-2016-1651
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Google
- **Affected Products:** Chrome
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-243/
## Vulnerability Details

This vulnerability allows an attacker to leak sensitive information on vulnerable installations of Google Chrome. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of JPEG2000 images. A specially crafted JPEG2000 image embedded inside a PDF can force Google Chrome to read memory past the end of an allocated object. An attacker can leverage this vulnerability to disclose the contents of adjacent memory.

## Additional Details

Google has issued an update to correct this vulnerability. More details can be found at: http://googlechromereleases.blogspot.com/2016/04/stable-channel-update_13.html

## Disclosure Timeline

- 2016-03-04 - Vulnerability reported to vendor
- 2016-04-15 - Coordinated public release of advisory
