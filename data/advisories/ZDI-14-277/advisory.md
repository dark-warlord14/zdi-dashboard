# ZDI-14-277: Adobe Flash Player Vector Object Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-277
- **ZDI-CAN:** ZDI-CAN-2326
- **Date:** 2014-08-12
- **CVE:** CVE-2014-0540
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Flash Player
- **Credit:** lokihardt@asrt
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-277/
## Vulnerability Details

This vulnerability allows remote attackers to disclose memory addresses on vulnerable installations of Adobe Flash. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of Vector objects. By manipulating Vector objects an attacker can read arbitrary memory. An attacker can leverage this vulnerability to leak arbitrary memory addresses.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://helpx.adobe.com/security/products/flash-player/apsb14-18.html

## Disclosure Timeline

- 2014-05-28 - Vulnerability reported to vendor
- 2014-08-12 - Coordinated public release of advisory
