# ZDI-16-453: Microsoft Windows xxxInsertMenuItem Out-Of-Bounds Access Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-453
- **ZDI-CAN:** ZDI-CAN-3767
- **Date:** 2016-08-09
- **CVE:** CVE-2016-3308
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Peter(Keen) and ZeguangZhao(team509)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-453/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of menu items. The issue lies in the failure to account for a special case in which there is ambiguity as to whether a specified menu item resides on a menu or on a submenu. An attacker can leverage this vulnerability to escalate privileges and execute code within the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS16-098

## Disclosure Timeline

- 2016-05-09 - Vulnerability reported to vendor
- 2016-08-09 - Coordinated public release of advisory
