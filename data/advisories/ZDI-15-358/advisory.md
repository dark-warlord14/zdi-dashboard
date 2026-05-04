# ZDI-15-358: BitTorrent/uTorrent URI Protocol Command Line Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-358
- **ZDI-CAN:** ZDI-CAN-2623
- **Date:** 2015-07-20
- **CVE:** CVE-2015-5474
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** BitTorrent BitTorrent
- **Affected Products:** uTorrent
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-358/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of BitTorrent and uTorrent. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The vulnerability relates to how BitTorrent and uTorrent handle URLs with the bittorrent or magnet protocol. By navigating the user to a specially formed link starting with bittorrent: or magnet:, an attacker can inject arbitrary command line parameters that will be passed to the BitTorrent or uTorrent executable. An attacker can leverage this vulnerability to execute code under the context of the current user.

## Additional Details

BitTorrent has issued an update to correct this vulnerability. More details can be found at: http://download-new.utorrent.com/uuid/1b11272b-e9c2-4f5a-aed5-cc23bcf7ef37 BitTorrent has issued an update to correct this vulnerability. More details can be found at: http://download-new.utorrent.com/uuid/1b11272b-e9c2-4f5a-aed5-cc23bcf7ef37

## Disclosure Timeline

- 2014-11-06 - Vulnerability reported to vendor
- 2015-07-20 - Coordinated public release of advisory
