# ZDI-20-143: Microsoft Windows WIA Junction Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-143
- **ZDI-CAN:** ZDI-CAN-9969
- **Date:** 2020-01-17
- **CVE:** CVE-2020-0635
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Glenn Lloyd
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-143/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Windows Image Acquisition service. By creating a junction, an attacker can abuse the service to overwrite the contents of a chosen file. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-0635

## Disclosure Timeline

- 2020-01-10 - Vulnerability reported to vendor
- 2020-01-17 - Coordinated public release of advisory
