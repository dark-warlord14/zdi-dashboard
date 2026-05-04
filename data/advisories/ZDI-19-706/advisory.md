# ZDI-19-706: Microsoft Windows CoreShellCOMServerRegistrar Improper Access Control Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-706
- **ZDI-CAN:** ZDI-CAN-7715
- **Date:** 2019-08-13
- **CVE:** CVE-2019-1184
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-706/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Core Shell COM Server Registrar application. By invoking a method of this DCOM component, an attacker can escalate privileges and execute arbitrary code in the context of the current user at medium integrity.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1184

## Disclosure Timeline

- 2019-01-25 - Vulnerability reported to vendor
- 2019-08-13 - Coordinated public release of advisory
