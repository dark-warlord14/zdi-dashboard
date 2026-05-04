# ZDI-22-879: ZyXel AP Configurator Incorrect Permission Assignment Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-879
- **ZDI-CAN:** ZDI-CAN-14791
- **Date:** 2022-06-29
- **CVE:** CVE-2022-0556
- **CVSS:** 7.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** ZyXel
- **Affected Products:** AP Configurator
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-879/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of ZyXel AP Configurator. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the installer. The issue results from incorrect permissions set on a directory. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of an Administrator.

## Additional Details

ZyXel has issued an update to correct this vulnerability. More details can be found at: https://www.zyxel.com/support/Zyxel-security-advisory-for-local-privilege-escalation-vulnerability-of-AP-Configurator.shtml

## Disclosure Timeline

- 2022-01-07 - Vulnerability reported to vendor
- 2022-06-29 - Coordinated public release of advisory
