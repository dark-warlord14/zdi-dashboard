# ZDI-12-058: Apple Quicktime PNG Depth Decoding Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-058
- **ZDI-CAN:** ZDI-CAN-1372
- **Date:** 2012-04-09
- **CVE:** CVE-2011-3460
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-058/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of AppleQuickTime Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw occurs when the application allocates space for decoding a video sample encoded with the .png format. When calculating space for this surface, the application will explicitly trust the bit-depth within the MediaVideo header. During the decoding process, the application will write outside the surface's boundaries. This can be leveraged to allow for one to earn code execution under the context of the application.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT5130

## Disclosure Timeline

- 2011-10-21 - Vulnerability reported to vendor
- 2012-04-09 - Coordinated public release of advisory
