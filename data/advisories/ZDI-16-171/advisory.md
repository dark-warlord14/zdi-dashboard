# ZDI-16-171: Google Chrome Pdfium JPEG2000 Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-171
- **ZDI-CAN:** ZDI-CAN-3432
- **Date:** 2016-02-18
- **CVE:** CVE-2016-1626
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Google
- **Affected Products:** Chrome
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-171/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Google Chrome. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of JPEG2000 images. A specially crafted JPEG2000 image embedded inside a PDF can force Google Chrome to read memory past the end of an allocated object. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Google has issued an update to correct this vulnerability. More details can be found at: http://googlechromereleases.blogspot.com/2016/02/stable-channel-update_9.html

## Disclosure Timeline

- 2015-12-21 - Vulnerability reported to vendor
- 2016-02-18 - Coordinated public release of advisory
