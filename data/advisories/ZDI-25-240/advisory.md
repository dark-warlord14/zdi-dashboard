# ZDI-25-240: Trend Micro Deep Security Anti-Malware Solution Platform Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-240
- **ZDI-CAN:** ZDI-CAN-24931
- **Date:** 2025-04-09
- **CVE:** CVE-2025-30641
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** Deep Security
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-240/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Trend Micro Deep Security Agent. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Anti-Malware Solution Platform. By creating a junction, an attacker can abuse the service to delete a folder. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/en-US/solution/KA-0019344

## Disclosure Timeline

- 2024-09-05 - Vulnerability reported to vendor
- 2025-04-09 - Coordinated public release of advisory
- 2025-04-09 - Advisory Updated
