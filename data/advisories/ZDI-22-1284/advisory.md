# ZDI-22-1284: Microsoft Windows DirectX Graphics Use-After-Free Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1284
- **ZDI-CAN:** ZDI-CAN-16686
- **Date:** 2022-09-19
- **CVE:** CVE-2022-37954
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1284/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the DirectX Graphics Kernel. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-37954

## Disclosure Timeline

- 2022-06-01 - Vulnerability reported to vendor
- 2022-09-19 - Coordinated public release of advisory
