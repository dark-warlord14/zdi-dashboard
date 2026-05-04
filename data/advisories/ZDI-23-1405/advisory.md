# ZDI-23-1405: Microsoft Windows CLFS Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1405
- **ZDI-CAN:** ZDI-CAN-20989
- **Date:** 2023-09-12
- **CVE:** CVE-2023-38144
- **CVSS:** 6.4
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:L/I:N/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1405/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the clfs.sys driver. A crafted BLF file can trigger can trigger a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-38144

## Disclosure Timeline

- 2023-05-23 - Vulnerability reported to vendor
- 2023-09-12 - Coordinated public release of advisory
