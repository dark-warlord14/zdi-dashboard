# ZDI-22-1033: Trend Micro Apex One Security Agent Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1033
- **ZDI-CAN:** ZDI-CAN-16692
- **Date:** 2022-07-28
- **CVE:** CVE-2022-36336
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** Abdelhamid Naceri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1033/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Apex One Security Agent. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the NT Apex One RealTime Scan Service. By creating a mount point, an attacker can abuse the service to delete a folder. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000291267

## Disclosure Timeline

- 2022-03-23 - Vulnerability reported to vendor
- 2022-07-28 - Coordinated public release of advisory
