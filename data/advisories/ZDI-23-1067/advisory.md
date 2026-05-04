# ZDI-23-1067: Microsoft Windows CLFS Incorrect Integer Conversion Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1067
- **ZDI-CAN:** ZDI-CAN-20977
- **Date:** 2023-08-14
- **CVE:** CVE-2023-36900
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1067/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the clfs.sys driver. A crafted BLF file can trigger an incorrect integer calculation before allocating a buffer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-36900

## Disclosure Timeline

- 2023-05-23 - Vulnerability reported to vendor
- 2023-08-14 - Coordinated public release of advisory
