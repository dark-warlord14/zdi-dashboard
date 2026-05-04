# ZDI-20-1372: Linux Kernel Performance Counters Race Condition Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1372
- **ZDI-CAN:** ZDI-CAN-11510
- **Date:** 2020-11-22
- **CVE:** CVE-2020-14351
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Ryota Shiga(@Ga_ryo_) of Flatt Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1372/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Linux Kernel. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the implementation of performance counters. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://access.redhat.com/security/cve/CVE-2020-14351

## Disclosure Timeline

- 2020-07-22 - Vulnerability reported to vendor
- 2020-11-22 - Coordinated public release of advisory
