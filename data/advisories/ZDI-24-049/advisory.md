# ZDI-24-049: D-Link DCS-8300LHV2 ONVIF Hardcoded PIN Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-049
- **ZDI-CAN:** ZDI-CAN-21492
- **Date:** 2024-01-11
- **CVE:** CVE-2023-51629
- **CVSS:** 6.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** D-Link
- **Affected Products:** DCS-8300LHV2
- **Credit:** Sina Kheirkhah (@SinSinology) of Summoning Team (@SummoningTeam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-049/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of D-Link DCS-8300LHV2 IP cameras. Authentication is not required to exploit this vulnerability. The specific flaw exists within the configuration of the ONVIF API. The issue results from the use of a hardcoded PIN. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

D-Link has issued an update to correct this vulnerability. More details can be found at: https://supportannouncement.us.dlink.com/announcement/publication.aspx?name=SAP10370

## Disclosure Timeline

- 2023-07-14 - Vulnerability reported to vendor
- 2024-01-11 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
