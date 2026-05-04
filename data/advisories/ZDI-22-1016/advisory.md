# ZDI-22-1016: (Pwn2Own) Inductive Automation Ignition Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1016
- **ZDI-CAN:** ZDI-CAN-17211
- **Date:** 2022-07-15
- **CVE:** CVE-2022-35869
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N
- **Affected Vendors:** Inductive Automation
- **Affected Products:** Ignition
- **Credit:** @_s_n_t of @pentestltd
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1016/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of Inductive Automation Ignition. Authentication is not required to exploit this vulnerability. The specific flaw exists within com.inductiveautomation.ignition.gateway.web.pages. The issue results from the lack of proper authentication prior to access to functionality. An attacker can leverage this vulnerability to bypass authentication on the system.

## Additional Details

Inductive Automation has issued an update to correct this vulnerability. More details can be found at: https://support.inductiveautomation.com/hc/en-us/articles/7625759776653-Regarding-Pwn2Own-2022-Vulnerabilities

## Disclosure Timeline

- 2022-05-09 - Vulnerability reported to vendor
- 2022-07-15 - Coordinated public release of advisory
