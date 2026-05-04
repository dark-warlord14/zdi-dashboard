# ZDI-21-019: Microsoft Windows Print Spooler Directory Junction Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-019
- **ZDI-CAN:** ZDI-CAN-11909
- **Date:** 2021-01-14
- **CVE:** CVE-2021-1695
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** JeongOh Kyea (@kkokkokye) of THEORI
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-019/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Print Spooler service. By creating a directory junction, an attacker can abuse the Print Spooler service to create a file in an arbitrary location. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-1695

## Disclosure Timeline

- 2020-09-25 - Vulnerability reported to vendor
- 2021-01-14 - Coordinated public release of advisory
