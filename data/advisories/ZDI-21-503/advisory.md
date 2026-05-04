# ZDI-21-503: Linux Kernel eBPF Improper Input Validation Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-503
- **ZDI-CAN:** ZDI-CAN-13661
- **Date:** 2021-05-03
- **CVE:** CVE-2021-31440
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Manfred Paul
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-503/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Linux Kernel. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of eBPF programs. The issue results from the lack of proper validation of user-supplied eBPF programs prior to executing them. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=10bf4e83167cc68595b85fd73bb91e8f2c086e36

## Disclosure Timeline

- 2021-04-23 - Vulnerability reported to vendor
- 2021-05-03 - Coordinated public release of advisory
