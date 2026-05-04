# ZDI-23-113: Microsoft Windows win32kfull Bitmap Use-After-Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-113
- **ZDI-CAN:** ZDI-CAN-19045
- **Date:** 2023-02-09
- **CVE:** CVE-2023-21532
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Marcin Wiazowski
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-113/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of bitmap objects. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21532

## Disclosure Timeline

- 2022-11-03 - Vulnerability reported to vendor
- 2023-02-09 - Coordinated public release of advisory
