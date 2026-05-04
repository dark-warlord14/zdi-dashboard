# ZDI-23-052: D-Link DIR-3040 MiniDLNA Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-052
- **ZDI-CAN:** ZDI-CAN-19910
- **Date:** 2023-01-18
- **CVE:** CVE-2022-43648
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** DIR-3040
- **Credit:** Nicholas Zubrisky
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-052/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of D-Link DIR-3040 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the MiniDLNA service. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the MiniDLNA service.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10322

## Disclosure Timeline

- 2022-12-23 - Vulnerability reported to vendor
- 2023-01-18 - Coordinated public release of advisory
