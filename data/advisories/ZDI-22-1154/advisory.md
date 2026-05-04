# ZDI-22-1154: (Pwn2Own) Softing Secure Integration Server wbemcomn Uncontrolled Search Path Element Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1154
- **ZDI-CAN:** ZDI-CAN-17234
- **Date:** 2022-08-23
- **CVE:** CVE-2022-2334
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Softing
- **Affected Products:** Secure Integration Server
- **Credit:** Chris Anastasio (muffin) and Steven Seeley (mr_me) of Incite Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1154/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of Softing Secure Integration Server. An attacker must first obtain the ability to execute high-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of project files. The service loads a DLL file from an unsecured location. An attacker can leverage this vulnerability to execute arbitrary code in the context of SYSTEM.

## Additional Details

Softing has issued an update to correct this vulnerability. More details can be found at: https://industrial.softing.com/fileadmin/psirt/downloads/syt-2022-5.html

## Disclosure Timeline

- 2022-05-10 - Vulnerability reported to vendor
- 2022-08-23 - Coordinated public release of advisory
