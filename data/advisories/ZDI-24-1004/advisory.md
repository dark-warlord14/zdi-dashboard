# ZDI-24-1004: (0Day) Avast Free Antivirus AvastSvc Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1004
- **ZDI-CAN:** ZDI-CAN-22963
- **Date:** 2024-07-29
- **CVE:** CVE-2024-7232
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Avast
- **Affected Products:** Free Antivirus
- **Credit:** Nicholas Zubrisky (@NZubrisky) and Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1004/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Avast Free Antivirus. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Avast Service. By creating a symbolic link, an attacker can abuse the service to delete a folder. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

1/03/24 – ZDI reported the vulnerability to Avast’s Security Reports team. 02/12/24 – ZDI asked for updates. 02/23/24 – ZDI asked for updates. 03/15/24 – ZDI informed the vendor that since we’ve not received a response that we will publish the case as a zero-day advisory on 03/27/24. 04/25/24 – A Gen Digital team member communicated that all the security issues should be submitted via a third-party Vulnerability Disclosure program 05/16/24 – ZDI resubmitted the vulnerability to the third-party Vulnerability Disclosure program 06/19/24 – ZDI asked for updates 07/26/24 – ZDI informed the vendor that since we’ve not received a response that we will publish the case as a zero-day advisory on 07/29/24 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2024-05-16 - Vulnerability reported to vendor
- 2024-07-29 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
