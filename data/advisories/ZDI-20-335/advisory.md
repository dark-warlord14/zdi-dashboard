# ZDI-20-335: (Pwn2Own) TP-Link Archer A7 File System Incorrect Permission Assignment for Critical Resource Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-335
- **ZDI-CAN:** ZDI-CAN-9651
- **Date:** 2020-03-25
- **CVE:** CVE-2020-10883
- **CVSS:** 5.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** TP-Link
- **Affected Products:** Archer A7
- **Credit:** Pedro Ribeiro and Radek Domanski of Team Flashback
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-335/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of TP-Link Archer A7 AC1750 routers. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the file system. The issue lies in the lack of proper permissions set on the file system. An attacker can leverage this vulnerability to escalate privileges.

## Additional Details

Fixed in version A7(US)_V5_200220

## Disclosure Timeline

- 2019-11-19 - Vulnerability reported to vendor
- 2020-03-25 - Coordinated public release of advisory
