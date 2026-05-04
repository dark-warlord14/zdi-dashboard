# ZDI-24-446: (0Day) D-Link G416 flupl self Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-446
- **ZDI-CAN:** ZDI-CAN-21294
- **Date:** 2024-05-24
- **CVE:** CVE-2024-5295
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** G416
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-446/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of D-Link G416 wireless routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the HTTP service listening on TCP port 80. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

08/16/23 – ZDI reported the vulnerabilities to the vendor 08/24/23 – The vendor communicated that the cases would be fixed in Q4, 2023 release 05/01/24 – ZDI notified the vendor of the intention to publish the case as 0-day advisory on 05/14/24 -- Mitigation: On May 14, 2024, the vendor informed ZDI about the software update v1.09B01 https://supportannouncement.us.dlink.com/security/publication.aspx?name=SAP10364

## Disclosure Timeline

- 2023-08-16 - Vulnerability reported to vendor
- 2024-05-24 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
