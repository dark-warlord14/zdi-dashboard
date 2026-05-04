# ZDI-20-995: Microsoft Windows Print Spooler Directory Junction Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-995
- **ZDI-CAN:** ZDI-CAN-11136
- **Date:** 2020-08-13
- **CVE:** CVE-2020-1337
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-995/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Print Spooler service. By creating a directory junction, an attacker can abuse the Print Spooler service to create an arbitrary file. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-1337

## Disclosure Timeline

- 2020-06-02 - Vulnerability reported to vendor
- 2020-08-13 - Coordinated public release of advisory
