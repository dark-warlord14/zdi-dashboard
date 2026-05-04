# ZDI-22-329: (Pwn2Own) Lexmark MC3224i setuid Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-329
- **ZDI-CAN:** ZDI-CAN-15895
- **Date:** 2022-02-15
- **CVE:** CVE-2021-44735
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Lexmark
- **Affected Products:** MC3224i
- **Credit:** David BERARD (@_p0ly_), Vincent FARGUES (@Karion_), Thomas IMBERT (@masthoon), from @Synacktiv
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-329/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Lexmark MC3224i printers. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the permissions set on root-owned service files. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

Lexmark has issued an update to correct this vulnerability. More details can be found at: https://publications.lexmark.com/publications/security-alerts/CVE-2021-44735.pdf

## Disclosure Timeline

- 2021-12-30 - Vulnerability reported to vendor
- 2022-02-15 - Coordinated public release of advisory
