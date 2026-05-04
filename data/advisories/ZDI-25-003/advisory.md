# ZDI-25-003: Trend Micro Apex One Security Agent Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-003
- **ZDI-CAN:** ZDI-CAN-24557
- **Date:** 2025-01-08
- **CVE:** CVE-2024-55632
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Apex One
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-003/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Apex One Security Agent. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Apex One NT RealTime Scan service. By creating a symbolic link, an attacker can abuse the service to create arbitrary files. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/en-US/solution/KA-0018217

## Disclosure Timeline

- 2024-07-03 - Vulnerability reported to vendor
- 2025-01-08 - Coordinated public release of advisory
- 2025-01-08 - Advisory Updated
