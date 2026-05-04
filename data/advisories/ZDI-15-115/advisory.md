# ZDI-15-115: BitTorrent Sync btsync: Protocol Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-115
- **ZDI-CAN:** ZDI-CAN-2624
- **Date:** 2015-04-03
- **CVE:** CVE-2015-2846
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** BitTorrent
- **Affected Products:** Sync
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-115/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of BitTorrent Sync. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how BitTorrent Sync handles URLs with the btsync protocol. By navigating the user to a specially formed link starting with btsync:, an attacker can inject arbitrary command line parameters that will be passed to BTSync.exe. An attacker can leverage this vulnerability to execute code under the context of the current user.

## Additional Details

BitTorrent has issued an update to correct this vulnerability. More details can be found at: https://www.getsync.com/

## Disclosure Timeline

- 2014-11-06 - Vulnerability reported to vendor
- 2015-04-03 - Coordinated public release of advisory
