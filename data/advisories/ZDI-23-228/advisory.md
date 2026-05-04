# ZDI-23-228: Ivanti Avalanche Remote Control Server RCServlet Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-228
- **ZDI-CAN:** ZDI-CAN-19513
- **Date:** 2023-03-09
- **CVE:** CVE-2022-44574
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ivanti
- **Affected Products:** Avalanche
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-228/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Ivanti Avalanche. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Remote Control Server RCServlet servlet. The issue results from the lack of authentication prior to allowing access to functionality. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Ivanti has issued an update to correct this vulnerability. More details can be found at: https://forums.ivanti.com/s/article/Avalanche-ZDI-CAN-19513-Security-Advisory?language=en_US

## Disclosure Timeline

- 2022-12-23 - Vulnerability reported to vendor
- 2023-03-09 - Coordinated public release of advisory
