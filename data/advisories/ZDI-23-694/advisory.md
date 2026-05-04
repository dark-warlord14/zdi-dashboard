# ZDI-23-694: Linux Kernel ksmbd RCU Callback Race Condition Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-694
- **ZDI-CAN:** ZDI-CAN-20477
- **Date:** 2023-05-17
- **CVE:** CVE-2023-32246
- **CVSS:** 5.0
- **CVSS Vector:** AV:L/AC:H/PR:H/UI:N/S:C/C:L/I:L/A:L
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Quentin Minster (@thalium_team)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-694/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on affected installations of Linux Kernel. An attacker must first obtain the ability to execute high-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of unloading of the ksmbd driver. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://github.com/torvalds/linux/commit/eb307d09fe15844fdaebeb8cc8c9b9e925430aa5

## Disclosure Timeline

- 2023-05-01 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory
