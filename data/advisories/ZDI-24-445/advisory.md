# ZDI-24-445: (0Day) D-Link DIR-3040 prog.cgi websSecurityHandler Memory Leak Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-445
- **ZDI-CAN:** ZDI-CAN-21668
- **Date:** 2024-05-24
- **CVE:** CVE-2024-5294
- **CVSS:** 4.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L
- **Affected Vendors:** D-Link
- **Affected Products:** DIR-3040
- **Credit:** Nicholas Zubrisky
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-445/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to create a denial-of-service condition on affected installations of D-Link DIR-3040 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the prog.cgi program, which handles HNAP requests made to the lighttpd webserver listening on ports 80 and 443. The issue results from the lack of proper memory management when processing HTTP cookie values. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

08/16/23 – ZDI reported the vulnerabilities to the vendor 08/24/23 – The vendor communicated that the cases would be fixed in Q4, 2023 release 05/01/24 – ZDI notified the vendor of the intention to publish the case as 0-day advisory on 05/14/24 -- Mitigation: On May 14, 2024, the vendor informed ZDI about the beta software update v120B03a Beta Hot-Fix https://supportannouncement.us.dlink.com/security/publication.aspx?name=SAP10387

## Disclosure Timeline

- 2023-08-16 - Vulnerability reported to vendor
- 2024-05-24 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
