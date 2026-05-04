# ZDI-20-949: FreeBSD Kernel sendmsg System Call Time-Of-Check Time-Of-Use Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-949
- **ZDI-CAN:** ZDI-CAN-11543
- **Date:** 2020-08-06
- **CVE:** CVE-2020-7460
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** FreeBSD
- **Affected Products:** Kernel
- **Credit:** m00nbsd
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-949/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of FreeBSD Kernel. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of arguments to the sendmsg system call. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the kernel.

## Additional Details

FreeBSD has issued an update to correct this vulnerability. More details can be found at: https://www.freebsd.org/security/advisories/FreeBSD-SA-20:23.sendmsg.asc

## Disclosure Timeline

- 2020-07-24 - Vulnerability reported to vendor
- 2020-08-06 - Coordinated public release of advisory
