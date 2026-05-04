# ZDI-23-439: Linux Kernel RxRPC Race Condition Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-439
- **ZDI-CAN:** ZDI-CAN-15975
- **Date:** 2023-04-13
- **CVE:** CVE-2023-2006
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Ayaz Mammadov (McYoloSwagHam)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-439/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Linux Kernel. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the processing of RxRPC bundles. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://git.kernel.org/pub/scm/linux/kernel/git/netdev/net.git/commit/?id=3bcd6c7eaa53

## Disclosure Timeline

- 2022-01-14 - Vulnerability reported to vendor
- 2023-04-13 - Coordinated public release of advisory
