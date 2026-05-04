# ZDI-17-845: Microsoft Windows Submenu Use-After-Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-845
- **ZDI-CAN:** ZDI-CAN-5199
- **Date:** 2017-10-10
- **CVE:** CVE-2017-8689
- **CVSS:** 7.2
- **CVSS Vector:** AV:L/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** hungtt28 & nyancat of Viettel Cyber Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-845/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the processing of hierarchical menus. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privilege to the level of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-8689

## Disclosure Timeline

- 2017-09-07 - Vulnerability reported to vendor
- 2017-10-10 - Coordinated public release of advisory
