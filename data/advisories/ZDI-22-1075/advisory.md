# ZDI-22-1075: Microsoft Windows win32kfull Bitmap Use-After-Free Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1075
- **ZDI-CAN:** ZDI-CAN-17679
- **Date:** 2022-08-18
- **CVE:** CVE-2022-35750
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Marcin Wiazowski
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1075/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of bitmap objects. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-35750

## Disclosure Timeline

- 2022-07-11 - Vulnerability reported to vendor
- 2022-08-18 - Coordinated public release of advisory
