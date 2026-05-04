# ZDI-23-004: Microsoft Windows GreStartDocInternal Use-After-Free Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-004
- **ZDI-CAN:** ZDI-CAN-18614
- **Date:** 2023-01-18
- **CVE:** CVE-2023-21680
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Marcin Wiazowski
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-004/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the GreStartDocInternal function. By making crafted calls into this function, an attacker can overflow the reference counter of a bitmap object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21680

## Disclosure Timeline

- 2022-09-30 - Vulnerability reported to vendor
- 2023-01-18 - Coordinated public release of advisory
