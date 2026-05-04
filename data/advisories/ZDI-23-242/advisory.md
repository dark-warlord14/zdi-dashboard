# ZDI-23-242: Microsoft Windows http.sys Integer Overflow Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-242
- **ZDI-CAN:** ZDI-CAN-19954
- **Date:** 2023-03-15
- **CVE:** CVE-2023-23410
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-242/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the http.sys kernel module. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before writing to memory. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-23410

## Disclosure Timeline

- 2023-01-04 - Vulnerability reported to vendor
- 2023-03-15 - Coordinated public release of advisory
