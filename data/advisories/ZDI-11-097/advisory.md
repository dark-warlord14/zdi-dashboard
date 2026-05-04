# ZDI-11-097: Apple Webkit setOuterText Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-097
- **ZDI-CAN:** ZDI-CAN-1009
- **Date:** 2011-03-02
- **CVE:** CVE-2011-0116
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Apple
- **Affected Products:** WebKit
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-097/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Webkit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the setOuterText method of the Webkit htmlelement library. Due to a failure to properly track DOM manipulations made within the browser, it is possible to make use of a previously freed pointer and facilitate remote code execution under the context of the user running the browser process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4554

## Disclosure Timeline

- 2010-12-21 - Vulnerability reported to vendor
- 2011-03-02 - Coordinated public release of advisory
