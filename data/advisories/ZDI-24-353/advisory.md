# ZDI-24-353: Softing edgeConnector Siemens Cleartext Transmission of Credentials Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-353
- **ZDI-CAN:** ZDI-CAN-20492
- **Date:** 2024-03-28
- **CVE:** CVE-2024-0860
- **CVSS:** 8.0
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Softing
- **Affected Products:** edgeConnector Siemens
- **Credit:** Pan ZhenPeng (@Peterpan0927) & Li JianTao (@CurseRed) of STAR Labs SG Pte. Ltd. (@starlabs_sg)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-353/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of Softing edgeConnector Siemens. Authentication is not required to exploit this vulnerability. The specific flaw exists within the web console, which listens on TCP port 8099 by default. HTTP traffic to this port contains unprotected credentials. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Softing has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-24-074-13

## Disclosure Timeline

- 2023-05-30 - Vulnerability reported to vendor
- 2024-03-28 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
