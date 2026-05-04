# ZDI-24-953: (0Day) Comodo Internet Security Pro Directory Traversal Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-953
- **ZDI-CAN:** ZDI-CAN-19055
- **Date:** 2024-07-23
- **CVE:** CVE-2024-7248
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Comodo
- **Affected Products:** Internet Security Pro
- **Credit:** Dennis Herrmann (@dhn_)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-953/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Comodo Internet Security Pro. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the update mechanism. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

11/21/22 – ZDI contacted Comodo and Xcitium support teams asking for their PISRT contact to responsibly disclose the issue 11/21/22 – Xcitium’s support team member advised ZDI to contact Comodo’s Subscriptions team for consumer products assistance 11/22/22 – ZDI sent a PISRT contact requests to Comodo’s Security and Subscriptions teams 06/23/23 – ZDI asked for updates 08/21/23 – ZDI notified the vendor of the intention to publish the cases as 0-day advisory 08/22/23 – Xcitium support team requested the vulnerability details 08/29/23 - ZDI submitted the vulnerability report to Xcitium support team 04/30/24 – ZDI asked for updates 05/01/24 – Xcitium’s support team rejected the report and advised ZDI to resubmit the report Comodo’s GeekBuddy Support team 05/03/24 – ZDI resubmitted the report Comodo’s GeekBuddy Support team 07/12/24 – ZDI asked for updates 07/12/24 - Comodo’s GeekBuddy Support team asked ZDI to submit the false positive file to Comodo’s Malware Analysis team 07/12/24 – ZDI notified the vendor of the intention to publish the cases as 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2023-08-29 - Vulnerability reported to vendor
- 2024-07-23 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
