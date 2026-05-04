# ZDI-22-1291: FreeBSD Kernel Netmap Time-Of-Check Time-Of-Use Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1291
- **ZDI-CAN:** ZDI-CAN-16683
- **Date:** 2022-09-20
- **CVE:** CVE-2022-23084
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** FreeBSD
- **Affected Products:** Kernel
- **Credit:** Lucas Leong (@_wmliang_) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1291/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of FreeBSD Kernel. An attacker must first obtain the ability to execute high-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of arguments to the Netmap device. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

FreeBSD has issued an update to correct this vulnerability. More details can be found at: https://www.freebsd.org/security/advisories/FreeBSD-SA-22:04.netmap.asc

## Disclosure Timeline

- 2022-02-18 - Vulnerability reported to vendor
- 2022-09-20 - Coordinated public release of advisory
