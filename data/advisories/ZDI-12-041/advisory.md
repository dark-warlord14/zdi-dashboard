# ZDI-12-041: Adobe Shockwave iml32.dll DEMX Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-041
- **ZDI-CAN:** ZDI-CAN-1247
- **Date:** 2012-03-01
- **CVE:** CVE-2011-2113
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Adobe
- **Affected Products:** Shockwave Player
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-041/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the Adobe Shockwave Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Shockwave 3d Asset.x32 module responsible for parsing 3D record types within RIFF-based Director files. The code within this module trusts invalid size checks to prevent integer wraps. Due to invalid compares, an integer overflow can occur when processing the data section of DEMX chunks, which subsequently leads to a heap-based buffer overflow. This can be leveraged to execute remote code under the context of the user running the browser.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb11-17.html

## Disclosure Timeline

- 2011-05-25 - Vulnerability reported to vendor
- 2012-03-01 - Coordinated public release of advisory
