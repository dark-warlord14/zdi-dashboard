# ZDI-20-350: (Pwn2Own) Linux Kernel eBPF Improper Input Validation Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-350
- **ZDI-CAN:** ZDI-CAN-10780
- **Date:** 2020-03-31
- **CVE:** CVE-2020-8835
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Manfred Paul of RedRocket CTF
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-350/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Linux Kernel. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of eBPF programs. The issue results from the lack of proper validation of user-supplied eBPF programs prior to executing them. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://www.openwall.com/lists/oss-security/2020/03/30/3

## Disclosure Timeline

- 2020-03-26 - Vulnerability reported to vendor
- 2020-03-31 - Coordinated public release of advisory
