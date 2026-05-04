# ZDI-24-1014: (0Day) Panda Security Dome VPN DLL Hijacking Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1014
- **ZDI-CAN:** ZDI-CAN-23428
- **Date:** 2024-07-29
- **CVE:** CVE-2024-7244
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Panda Security
- **Affected Products:** Dome
- **Credit:** Nicholas Zubrisky (@NZubrisky) and Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1014/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Panda Security Dome. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the VPN process. The process does not restrict DLL search to trusted paths, which can result in the loading of a malicious DLL. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

02/14/24 – ZDI reported the vulnerability to WatchGuard PSIRT 06/26/24 – ZDI asked for updates. 07/26/24 – ZDI informed the vendor that since we have not received a response that we will publish the reports as zero-day advisories on 07/29/24 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application

## Disclosure Timeline

- 2024-02-14 - Vulnerability reported to vendor
- 2024-07-29 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
