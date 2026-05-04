# ZDI-12-057: (Pwn2Own) Adobe Flash Player NetStream addBytes Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-057
- **ZDI-CAN:** ZDI-CAN-1548
- **Date:** 2012-04-09
- **CVE:** N/A
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Adobe
- **Affected Products:** Flash Player
- **Credit:** VUPEN Vulnerability Research Team http://www.vupen.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-057/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Flash Player handles the update of a NetStream object via the appendBytes method which can lead to a use-after-free condition when the function returns. This can result in remote code execution under the context of the current process.

## Additional Details

http://www.adobe.com/support/security/bulletins/apsb12-07.html

## Disclosure Timeline

- 2012-03-12 - Vulnerability reported to vendor
- 2012-04-09 - Coordinated public release of advisory
