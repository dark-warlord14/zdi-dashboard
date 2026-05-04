# ZDI-23-1512: (0Day) D-Link D-View coreservice_action_script Exposed Dangerous Function Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1512
- **ZDI-CAN:** ZDI-CAN-19573
- **Date:** 2023-10-04
- **CVE:** CVE-2023-44414
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** D-Link
- **Affected Products:** D-View
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1512/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of D-Link D-View. Authentication is not required to exploit this vulnerability. The specific flaw exists within the coreservice_action_script action. The issue results from the exposure of a dangerous function. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

12/23/22 – The ZDI reported the vulnerability to the vendor. 08/25/23 – ZDI asked for an update. 08/30/23 – The vendor states they don’t have the case on record. 08/31/23 – ZDI forwarded the original report to the vendor. 09/29/23 – The ZDI informed the vendor that the case will be published as a zero-day advisory on 10/04/23. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2022-12-23 - Vulnerability reported to vendor
- 2023-10-04 - Coordinated public release of advisory
