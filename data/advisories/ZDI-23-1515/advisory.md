# ZDI-23-1515: (0Day) D-Link DAP-2622 DDP Set IPv4 Address Auth Password Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1515
- **ZDI-CAN:** ZDI-CAN-20091
- **Date:** 2023-10-04
- **CVE:** CVE-2023-44417
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** DAP-2622
- **Credit:** Dmitry "InfoSecDJ" Janushkevich of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1515/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of D-Link DAP-2622 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the DDP service. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

01/20/23 – ZDI reported the vulnerability to the vendor. 06/05/23 – The vendor informed us that some of the reports were missing. 06/19/23 – ZDI sent over the missing reports. 08/24/23 – The vendor released an update for DAP-2622, but this case was missing. 08/31/23 – ZDI informed the vendor that the case was not included in the update. 09/29/23 – The ZDI informed the vendor that the case will be published as a zero-day advisory on 10/04/23. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2023-01-20 - Vulnerability reported to vendor
- 2023-10-04 - Coordinated public release of advisory
