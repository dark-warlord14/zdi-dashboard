# ZDI-16-353: BitTorrent API Cross Site Scripting Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-353
- **ZDI-CAN:** ZDI-CAN-3544
- **Date:** 2016-05-20
- **CVE:** N/A
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** BitTorrent
- **Affected Products:** BitTorrent
- **Credit:** lokihardt
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-353/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of BitTorrent and uTorrent. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. These applications expose a web service locally on port 10000. An attacker can use a cross site scripting vulnerability in this web service to obtain a credential allowing full access to the web service. An attacker can leverage this to execute code under the context of the current user.

## Additional Details

BitTorrent has issued an update to correct this vulnerability. More details can be found at: http://download-01.utorrent.com/uuid/bafd4502-33a8-4ce4-9720-2183638e4281

## Disclosure Timeline

- 2016-02-01 - Vulnerability reported to vendor
- 2016-05-20 - Coordinated public release of advisory
