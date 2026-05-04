# ZDI-07-036: Arris Cadant C3 CMTS Remote DoS Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-036
- **ZDI-CAN:** ZDI-CAN-149
- **Date:** 2007-06-11
- **CVE:** CVE-2007-2796
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Arris
- **Affected Products:** Cadant C3 CMTS
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-036/
## Vulnerability Details

This vulnerability allows remote attackers to cause a denial of service on vulnerable Arris Cadant C3 CMTS systems. Authentication is not required to exploit this vulnerability. The flaw exists due to mishandling of IP options. When an unknown or bad option is specified, the C3 will terminate disabling all service that is handled by that CMTS. The vulnerability can be triggered with a single malformed IP packet.

## Additional Details

Arris has issued an update to correct this vulnerability. More details can be found at: http://www.arrisi.com/contact_us/support/

## Disclosure Timeline

- 2007-02-23 - Vulnerability reported to vendor
- 2007-06-11 - Coordinated public release of advisory
