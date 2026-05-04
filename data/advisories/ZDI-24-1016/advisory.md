# ZDI-24-1016: (0Day) Panda Security Dome Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1016
- **ZDI-CAN:** ZDI-CAN-23375
- **Date:** 2024-07-29
- **CVE:** CVE-2024-7241
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Panda Security
- **Affected Products:** Dome
- **Credit:** Nicholas Zubrisky (@NZubrisky) and Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1016/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Panda Security Dome. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the PSANHost service. By creating a junction, an attacker can abuse the service to create an arbitrary file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

02/06/24 – ZDI reported the vulnerability to the vendor’s Security team. 02/06/24 – The vendor’s Security team advised ZDI to resubmit the report to WatchGuard PSIRT 02/13/24 – ZDI resubmitted the report to WatchGuard PSIRT 06/19/24 – ZDI asked for updates and notified the vendor of the intention to publish the cases as 0-day advisory 07/26/24 – ZDI informed the vendor that since we have not received a response that we will publish the report as zero-day advisory on 07/29/2 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application

## Disclosure Timeline

- 2024-02-06 - Vulnerability reported to vendor
- 2024-07-29 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
