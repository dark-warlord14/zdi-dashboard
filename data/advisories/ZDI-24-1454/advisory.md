# ZDI-24-1454: Linux Kernel nftables Improper Validation of Array Index Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1454
- **ZDI-CAN:** ZDI-CAN-24184
- **Date:** 2024-11-05
- **CVE:** N/A
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Kuan-Ting Chen (@h3xr4bb1t) of DEVCORE Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1454/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of the Linux Kernel. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of packet filtering tables. The issue results from the lack of proper validation of user-supplied data, which can result in a memory access past the end of an allocated array. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://cdn.kernel.org/pub/linux/kernel/v5.x/ChangeLog-5.10.221

## Disclosure Timeline

- 2024-06-21 - Vulnerability reported to vendor
- 2024-11-05 - Coordinated public release of advisory
- 2024-11-05 - Advisory Updated
