# ZDI-23-1766: Extreme Networks AP410C ah_webui Missing Authentication for Critical Function Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1766
- **ZDI-CAN:** ZDI-CAN-20530
- **Date:** 2023-12-12
- **CVE:** CVE-2023-46271
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Extreme Networks
- **Affected Products:** AP410C
- **Credit:** Victorien Molle - Biche Télécom
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1766/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to reach critical functions on affected installations of Extreme Networks AP410C routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ah_webui service, which listens on TCP port 3009 by default. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code within the context of root.

## Additional Details

Extreme Networks has issued an update to correct this vulnerability. More details can be found at: https://extreme-networks.my.site.com/ExtrArticleDetail?an=000115354&q=CVE-2023-46271

## Disclosure Timeline

- 2023-07-06 - Vulnerability reported to vendor
- 2023-12-12 - Coordinated public release of advisory
