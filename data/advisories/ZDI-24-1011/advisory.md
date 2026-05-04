# ZDI-24-1011: (0Day) VIPRE Advanced Security SBAMSvc Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1011
- **ZDI-CAN:** ZDI-CAN-22238
- **Date:** 2024-07-29
- **CVE:** CVE-2024-7238
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** VIPRE
- **Affected Products:** Advanced Security
- **Credit:** Nicholas Zubrisky and Michael DePlante (@izobashi) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1011/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of VIPRE Advanced Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Anti Malware Service. By creating a symbolic link, an attacker can abuse the service to delete a file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

10/12/23 – ZDI submitted the vulnerability to the vendor via a third-party Vulnerability Disclosure program 10/18/23 – The third-party Vulnerability Disclosure program mentioned that the reported issue was out of scope the program’s and closed the report as Not Applicable 10/18/23 – ZDI asked for reasons 10/18/23 – The vendor confirmed that the issue was being investigated and confirmed the vulnerability was in the Vulnerability Disclosure program’s scope 10/19/23:01/16/24 - ZDI has provided multiple instructions, PoCs and answers to help the third-party program to reproduce the issue 01/31/23 – The third-party Vulnerability Disclosure program marked the report as not applicable and not being a rewardable submission 01/17/24 – ZDI communicated that rewards and bounties have never been accepted by Trend Micro Zero Day Initiative and notified the vendor of the intention to publish the cases as 0-day advisory 07/26/24 – ZDI notified the vendor of the intention to publish the cases as 0-day advisory on 07/29/24 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application

## Disclosure Timeline

- 2023-10-12 - Vulnerability reported to vendor
- 2024-07-29 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
