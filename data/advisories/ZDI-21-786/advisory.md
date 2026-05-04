# ZDI-21-786: Trend Micro Apex One Incorrect Permission Assignment Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-786
- **ZDI-CAN:** ZDI-CAN-12151
- **Date:** 2021-07-13
- **CVE:** CVE-2021-32463
- **CVSS:** 6.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** Lynn
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-786/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of Trend Micro Apex One. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Security Agent. The issue results from incorrect permissions set on a resource used by the service. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000286855

## Disclosure Timeline

- 2021-03-12 - Vulnerability reported to vendor
- 2021-07-13 - Coordinated public release of advisory
