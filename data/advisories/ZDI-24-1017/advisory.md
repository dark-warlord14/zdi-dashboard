# ZDI-24-1017: (0Day) Panda Security Dome Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1017
- **ZDI-CAN:** ZDI-CAN-23402
- **Date:** 2024-07-29
- **CVE:** CVE-2024-7242
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Panda Security
- **Affected Products:** Dome
- **Credit:** Nicholas Zubrisky (@NZubrisky) and Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1017/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Panda Security Dome. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the PSANHost executable. By creating a junction, an attacker can abuse the service to delete arbitrary files. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

02/14/24 – ZDI reported the vulnerability to WatchGuard PSIRT 06/26/24 – ZDI asked for updates. 07/26/24 – ZDI informed the vendor that since we have not received a response that we will publish the reports as zero-day advisories on 07/29/24 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application

## Disclosure Timeline

- 2024-02-14 - Vulnerability reported to vendor
- 2024-07-29 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
