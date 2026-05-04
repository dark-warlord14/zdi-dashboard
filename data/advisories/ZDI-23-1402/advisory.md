# ZDI-23-1402: Hewlett Packard Enterprise OneView resetAdminPassword Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1402
- **ZDI-CAN:** ZDI-CAN-21510
- **Date:** 2023-09-11
- **CVE:** CVE-2023-30908
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** OneView
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1402/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Hewlett Packard Enterprise OneView. Authentication is not required to exploit this vulnerability. The specific flaw exists within the resetAdminPassword endpoint. The issue results from the lack of proper validation of the attacker's IP address. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: https://support.hpe.com/hpesc/public/docDisplay?docLocale=en_US&docId=hpesbgn04530en_us

## Disclosure Timeline

- 2023-07-26 - Vulnerability reported to vendor
- 2023-09-11 - Coordinated public release of advisory
