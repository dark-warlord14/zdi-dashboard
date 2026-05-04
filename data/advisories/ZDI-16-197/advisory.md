# ZDI-16-197: Google Chrome Pdfium JPEG2000 Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-197
- **ZDI-CAN:** ZDI-CAN-3563
- **Date:** 2016-03-10
- **CVE:** CVE-2016-1645
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Google
- **Affected Products:** Chrome
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-197/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Google Chrome. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of JPEG2000 images. A specially crafted JPEG2000 image embedded inside a PDF can force Google Chrome to write memory past the end of an allocated object. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Google has issued an update to correct this vulnerability. More details can be found at: http://googlechromereleases.blogspot.com/2016/03/stable-channel-update_8.html

## Disclosure Timeline

- 2016-02-16 - Vulnerability reported to vendor
- 2016-03-10 - Coordinated public release of advisory
