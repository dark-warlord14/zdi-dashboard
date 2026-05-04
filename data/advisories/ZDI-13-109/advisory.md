# ZDI-13-109: Webkit.org Webkit string.replace Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-109
- **ZDI-CAN:** ZDI-CAN-1517
- **Date:** 2013-05-30
- **CVE:** CVE-2013-0999
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** WebKit.Org
- **Affected Products:** WebKit
- **Credit:** pa_kt / twitter.com/pa_kt
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-109/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Webkit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Webkit implements the string.replace() method. Due to insufficient boundary checks it is possible for specially crafted strings to cause an int wrap during the calculation of a buffer size. This could lead to a heap buffer overflow that could result in remote code execution under the context of the current user.

## Additional Details

WebKit.Org has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT1222

## Disclosure Timeline

- 2012-11-21 - Vulnerability reported to vendor
- 2013-05-30 - Coordinated public release of advisory
