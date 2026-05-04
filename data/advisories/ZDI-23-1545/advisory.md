# ZDI-23-1545: Microsoft Windows IsSurfaceLockable Type Confusion Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1545
- **ZDI-CAN:** ZDI-CAN-21161
- **Date:** 2023-10-11
- **CVE:** CVE-2023-36594
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Marcin Wiazowski
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1545/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. Additionally, the target system must have multiple active monitors. The specific flaw exists within the IsSurfaceLockable function in the win32kfull driver. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-36594

## Disclosure Timeline

- 2023-06-29 - Vulnerability reported to vendor
- 2023-10-11 - Coordinated public release of advisory
