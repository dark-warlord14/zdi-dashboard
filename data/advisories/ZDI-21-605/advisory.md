# ZDI-21-605: SolarWinds Orion Job Scheduler JobRouterService Improper Authorization Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-605
- **ZDI-CAN:** ZDI-CAN-12007
- **Date:** 2021-05-21
- **CVE:** CVE-2021-31475
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** SolarWinds
- **Affected Products:** Orion Job Scheduler
- **Credit:** Harrison Neal
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-605/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of SolarWinds Orion Job Scheduler. Authentication is required to exploit this vulnerability. The specific flaw exists within the JobRouterService WCF service. The issue is due to the WCF service configuration, which allows a critical resource to be accessed by unprivileged users. An attacker can leverage this vulnerability to execute code in the context of an administrator.

## Additional Details

SolarWinds has issued an update to correct this vulnerability. More details can be found at: https://documentation.solarwinds.com/en/success_center/orionplatform/content/release_notes/orion_platform_2020-2-5_release_notes.htm

## Disclosure Timeline

- 2021-01-22 - Vulnerability reported to vendor
- 2021-05-21 - Coordinated public release of advisory
