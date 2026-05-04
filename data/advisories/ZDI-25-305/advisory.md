# ZDI-25-305: Apple XNU kernel vm_map Race Condition Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-305
- **ZDI-CAN:** ZDI-CAN-24156
- **Date:** 2025-05-21
- **CVE:** CVE-2025-31219
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** XNU kernel
- **Credit:** Michael DePlante (@izobashi) and Lucas Leong (@_wmliang_) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-305/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of virtual memory allocations in the macOS kernel. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/122716

## Disclosure Timeline

- 2025-02-13 - Vulnerability reported to vendor
- 2025-05-21 - Coordinated public release of advisory
- 2025-05-21 - Advisory Updated
