# ZDI-24-1035: Microsoft Windows NTFS Junction Heap-based Buffer Overflow Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1035
- **ZDI-CAN:** ZDI-CAN-22668
- **Date:** 2024-07-31
- **CVE:** CVE-2024-21371
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1035/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of NTFS junctions. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2024-21371

## Disclosure Timeline

- 2024-02-06 - Vulnerability reported to vendor
- 2024-07-31 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
