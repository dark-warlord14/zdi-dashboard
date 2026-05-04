# ZDI-24-1648: Linux Kernel Bluetooth HCI Request Race Condition Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1648
- **ZDI-CAN:** ZDI-CAN-24547
- **Date:** 2024-12-10
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:L/AC:H/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Lucas Leong (@_wmliang_) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1648/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Linux Kernel. An attacker must first obtain the ability to execute high-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of Bluetooth socket buffers. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://git.kernel.org/pub/scm/linux/kernel/git/bluetooth/bluetooth-next.git/commit/?id=92048ab2e2e6

## Disclosure Timeline

- 2024-06-21 - Vulnerability reported to vendor
- 2024-12-10 - Coordinated public release of advisory
- 2024-12-10 - Advisory Updated
