# ZDI-24-1194: Linux Kernel Plan 9 File System Race Condition Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1194
- **ZDI-CAN:** ZDI-CAN-24058
- **Date:** 2024-09-05
- **CVE:** CVE-2024-39463
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Meysam Firouzi @R00tkitSMM and Amirmohammad Eftekhar @zer0legday
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1194/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Linux Kernel. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of the p9_fid object. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://lore.kernel.org/linux-cve-announce/2024062513-CVE-2024-39463-42c8@gregkh/T/

## Disclosure Timeline

- 2024-05-19 - Vulnerability reported to vendor
- 2024-09-05 - Coordinated public release of advisory
- 2024-09-05 - Advisory Updated
