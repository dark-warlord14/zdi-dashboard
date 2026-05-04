# ZDI-24-031: Microsoft Windows cldflt Integer Overflow Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-031
- **ZDI-CAN:** ZDI-CAN-22126
- **Date:** 2024-01-10
- **CVE:** CVE-2024-21310
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-031/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. Only systems with long Win32 path support enabled are affected. The specific flaw exists within the cldflt.sys driver. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-21310

## Disclosure Timeline

- 2023-10-03 - Vulnerability reported to vendor
- 2024-01-10 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
