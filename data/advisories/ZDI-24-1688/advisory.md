# ZDI-24-1688: Linux Kernel ksmbd PreviousSessionId Race Condition Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1688
- **ZDI-CAN:** ZDI-CAN-25040
- **Date:** 2024-12-12
- **CVE:** N/A
- **CVSS:** 8.5
- **CVSS Vector:** AV:N/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** fffvr
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1688/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Linux Kernel. Authentication is required to exploit this vulnerability. However, only systems with ksmbd enabled are vulnerable. The specific flaw exists within the processing of sessions with PreviousSessionId. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to execute code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://lore.kernel.org/all/CAKYAXd_MPF9WiFoOwnPBiPvwMKDjGJ4BX4u-UnGymFM4sp3YMQ@mail.gmail.com/T/

## Disclosure Timeline

- 2024-08-14 - Vulnerability reported to vendor
- 2024-12-12 - Coordinated public release of advisory
- 2024-12-12 - Advisory Updated
