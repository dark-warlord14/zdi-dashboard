# ZDI-19-360: Microsoft Windows AppX Deployment Service Hard Link Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-360
- **ZDI-CAN:** ZDI-CAN-7753
- **Date:** 2019-04-15
- **CVE:** CVE-2019-0841
- **CVSS:** 7.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-360/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the AppX Deployment Service. By creating a hard link, an attacker can abuse the service to weaken the ACL of a chosen file. An attacker can leverage this vulnerability to escalate privileges to resources normally protected from the current user or app.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0841

## Disclosure Timeline

- 2018-12-29 - Vulnerability reported to vendor
- 2019-04-15 - Coordinated public release of advisory
