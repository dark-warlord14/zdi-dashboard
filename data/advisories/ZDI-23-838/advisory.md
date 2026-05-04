# ZDI-23-838: NETGEAR RAX30 Use of Hard-coded Credentials Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-838
- **ZDI-CAN:** ZDI-CAN-19660
- **Date:** 2023-06-08
- **CVE:** CVE-2023-34284
- **CVSS:** 6.3
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** NETGEAR
- **Affected Products:** RAX30
- **Credit:** Dmitry "InfoSecDJ" Janushkevich of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-838/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass authentication on affected installations of NETGEAR RAX30 routers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the system configuration. The system contains a hardcoded user account which can be used to access the CLI service as a low-privileged user. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

NETGEAR has issued an update to correct this vulnerability. More details can be found at: https://kb.netgear.com/000065650/Security-Advisory-for-Multiple-Vulnerabilities-on-the-RAX30-PSV-2023-0003-PSV-2023-0004?article=000065650

## Disclosure Timeline

- 2023-01-04 - Vulnerability reported to vendor
- 2023-06-08 - Coordinated public release of advisory
