# ZDI-24-954: (0Day) Comodo Firewall Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-954
- **ZDI-CAN:** ZDI-CAN-21794
- **Date:** 2024-07-23
- **CVE:** CVE-2024-7249
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Comodo
- **Affected Products:** Firewall
- **Credit:** Amol Dosanjh of Trend Micro and Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-954/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Comodo Firewall. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the cmdagent executable. By creating a symbolic link, an attacker can abuse the application to delete a file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

08/29/23 – ZDI submitted the vulnerability report to Xcitium support team 04/30/24 – ZDI asked for updates 05/01/24 – Xcitium’s support team rejected the report and advised ZDI to resubmit the report Comodo’s GeekBuddy Support team 05/03/24 – ZDI resubmitted the report Comodo’s GeekBuddy Support team 07/12/24 – ZDI asked for updates 07/12/24 - Comodo’s GeekBuddy Support team asked ZDI to submit the false positive file to Comodo’s Malware Analysis team 07/12/24 – ZDI notified the vendor of the intention to publish the cases as 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2023-08-29 - Vulnerability reported to vendor
- 2024-07-23 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
