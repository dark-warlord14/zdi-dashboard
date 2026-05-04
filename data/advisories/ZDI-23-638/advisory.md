# ZDI-23-638: Schneider Electric APC Easy UPS Online SNMPDBManager Use of Hard-Coded Credentials Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-638
- **ZDI-CAN:** ZDI-CAN-17585
- **Date:** 2023-05-17
- **CVE:** CVE-2022-42973
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Schneider Electric
- **Affected Products:** APC Easy UPS Online
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-638/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Schneider Electric APC Easy UPS Online. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the SNMPDBManager class. The issue results from the use of hard-coded credentials. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-22-347-02

## Disclosure Timeline

- 2022-06-17 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory
