# ZDI-24-020: Linux Kernel GSM Multiplexing Race Condition Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-020
- **ZDI-CAN:** ZDI-CAN-20527
- **Date:** 2024-01-09
- **CVE:** CVE-2023-6546
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Nassim Asrir
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-020/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on affected installations of Linux Kernel. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the n_gsm driver. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://github.com/torvalds/linux/commit/3c4f8333b582487a2d1e02171f1465531cde53e3

## Disclosure Timeline

- 2023-04-06 - Vulnerability reported to vendor
- 2024-01-09 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
