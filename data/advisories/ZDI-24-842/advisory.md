# ZDI-24-842: Linux Kernel ICMPv6 Router Advertisement Race Condition Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-842
- **ZDI-CAN:** ZDI-CAN-22579
- **Date:** 2024-06-21
- **CVE:** CVE-2023-6200
- **CVSS:** 8.3
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Lucas Leong (@_wmliang_) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-842/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Linux Kernel. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of Route Information options. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to execute code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://bugzilla.redhat.com/show_bug.cgi?id=2250377

## Disclosure Timeline

- 2023-11-16 - Vulnerability reported to vendor
- 2024-06-21 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
