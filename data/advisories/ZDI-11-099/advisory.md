# ZDI-11-099: Apple Webkit Font Glyph Layout Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-099
- **ZDI-CAN:** ZDI-CAN-968
- **Date:** 2011-03-02
- **CVE:** CVE-2011-0133
- **CVSS:** 9.7
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:P/A:C
- **Affected Vendors:** Apple
- **Affected Products:** WebKit
- **Credit:** wushi of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-099/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari's Webkit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way the application handles floating blocks in certain situations. When performing layout operations for a floating block produced by a pseudo-element, the application will attempt to access glyph data that hasn't been fully assigned into the glyph data hashmap. Due to this type being incomplete, this can lead to code execution under the context of the application.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4554

## Disclosure Timeline

- 2010-10-18 - Vulnerability reported to vendor
- 2011-03-02 - Coordinated public release of advisory
