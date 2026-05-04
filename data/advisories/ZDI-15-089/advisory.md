# ZDI-15-089: Google Chrome V8EventListenerList::findOrCreateWrapper Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-089
- **ZDI-CAN:** ZDI-CAN-2662
- **Date:** 2015-03-12
- **CVE:** CVE-2015-1230
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Google
- **Affected Products:** Chrome
- **Credit:** SkyLined
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-089/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Google Chrome. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within findOrCreateWrapper. By manipulating a document's elements, an attacker can force a type confusion error while adding an event listener. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Google has issued an update to correct this vulnerability. More details can be found at: http://googlechromereleases.blogspot.com/2015/03/stable-channel-update.html

## Disclosure Timeline

- 2015-01-16 - Vulnerability reported to vendor
- 2015-03-12 - Coordinated public release of advisory
