# ZDI-16-674: BitTorrent API Cross-Site Scripting Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-674
- **ZDI-CAN:** ZDI-CAN-4050
- **Date:** 2016-12-26
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** BitTorrent
- **Affected Products:** BitTorrent
- **Credit:** Simon Zuckerbraun - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-674/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of BitTorrent and uTorrent. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. These applications expose a web service locally on port 10000. An attacker can use a cross site scripting vulnerability in this web service to obtain a credential allowing full access to the web service. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current user.

## Additional Details

BitTorrent has issued an update to correct this vulnerability. More details can be found at: http://blog.utorrent.com/releases/windows/

## Disclosure Timeline

- 2016-10-17 - Vulnerability reported to vendor
- 2016-12-26 - Coordinated public release of advisory
