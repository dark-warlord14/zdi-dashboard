# ZDI-11-240: Apple Safari Webkit SVG Marker Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-240
- **ZDI-CAN:** ZDI-CAN-1021
- **Date:** 2011-07-27
- **CVE:** CVE-2011-1453
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** WebKit
- **Credit:** wushi of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-240/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari's Webkit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the library's support of SVG markers. When updating a marker, the application will duplicate the reference of an object without updating it's reference count. When freeing this object, a use-after-free vulnerability can be made to occur. This can be leveraged by a remote attacker to execute code under the context of the user running the application.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4808

## Disclosure Timeline

- 2011-01-21 - Vulnerability reported to vendor
- 2011-07-27 - Coordinated public release of advisory
