# ZDI-13-108: Webkit.org Webkit string.concat() Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-108
- **ZDI-CAN:** ZDI-CAN-1516
- **Date:** 2013-05-30
- **CVE:** CVE-2013-0998
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** WebKit.Org
- **Affected Products:** WebKit
- **Credit:** pa_kt / twitter.com/pa_kt
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-108/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Webkit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Webkit implements string.concat(). When concatenating multiple strings the function fails to properly check for overflows and as such is vulnerable to heap corruption. This could result in remote code execution under the context of the current program.

## Additional Details

WebKit.Org has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT1222

## Disclosure Timeline

- 2012-11-21 - Vulnerability reported to vendor
- 2013-05-30 - Coordinated public release of advisory
