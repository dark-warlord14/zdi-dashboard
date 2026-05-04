# ZDI-23-1765: Extreme Networks HiveOS ah_auth Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1765
- **ZDI-CAN:** ZDI-CAN-20728
- **Date:** 2023-12-12
- **CVE:** CVE-2023-46272
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Extreme Networks
- **Affected Products:** HiveOS
- **Credit:** Victorien Molle - Biche Télécom
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1765/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Extreme Networks routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ah_auth service, which listens on UDP port 3001. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Extreme Networks has issued an update to correct this vulnerability. More details can be found at: https://extreme-networks.my.site.com/ExtrArticleDetail?an=000115355&q=CVE-2023-46272

## Disclosure Timeline

- 2023-07-06 - Vulnerability reported to vendor
- 2023-12-12 - Coordinated public release of advisory
