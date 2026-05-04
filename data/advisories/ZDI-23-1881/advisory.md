# ZDI-23-1881: (0Day) Voltronic Power ViewPower MonitorConsole Exposed Dangerous Method Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1881
- **ZDI-CAN:** ZDI-CAN-22011
- **Date:** 2023-12-20
- **CVE:** CVE-2023-51575
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Voltronic Power
- **Affected Products:** ViewPower
- **Credit:** hir0ot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1881/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Voltronic Power ViewPower. Authentication is not required to exploit this vulnerability. The specific flaw exists within the MonitorConsole class. The issue results from an exposed dangerous method. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

08/03/23 – ZDI made multiple attempts to contact the vendor across sales, support, and professional networking channels, which yielded no response from the vendor. We also contacted CISA, who was unsuccessful in receiving a response from the vendor. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2023-11-17 - Vulnerability reported to vendor
- 2023-12-20 - Coordinated public release of advisory
