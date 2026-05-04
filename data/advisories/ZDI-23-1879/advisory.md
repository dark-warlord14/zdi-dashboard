# ZDI-23-1879: (0Day) Voltronic Power ViewPower Pro updateManagerPassword Exposed Dangerous Function Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1879
- **ZDI-CAN:** ZDI-CAN-21203
- **Date:** 2023-12-20
- **CVE:** CVE-2023-51573
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Voltronic Power
- **Affected Products:** ViewPower Pro
- **Credit:** Simon Janz (@esj4y)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1879/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Voltronic Power ViewPower Pro. Authentication is not required to exploit this vulnerability. The specific flaw exists within the updateManagerPassword function. The issue results from the exposure of a dangerous function. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

08/03/23 – ZDI made multiple attempts to contact the vendor across sales, support, and professional networking channels, which yielded no response from the vendor. We also contacted CISA, who was unsuccessful in receiving a response from the vendor. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2023-08-03 - Vulnerability reported to vendor
- 2023-12-20 - Coordinated public release of advisory
