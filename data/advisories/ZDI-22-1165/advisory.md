# ZDI-22-1165: Linux Kernel Watch Queue Race Condition Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1165
- **ZDI-CAN:** ZDI-CAN-17291
- **Date:** 2022-08-24
- **CVE:** CVE-2022-2959
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Selim Enes Karaduman @Enesdex
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1165/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Linux Kernel. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of pipe buffers. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://access.redhat.com/security/cve/CVE-2022-2959

## Disclosure Timeline

- 2022-05-25 - Vulnerability reported to vendor
- 2022-08-24 - Coordinated public release of advisory
