# ZDI-23-442: Linux Kernel netdevsim Improper Update of Reference Count Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-442
- **ZDI-CAN:** ZDI-CAN-17811
- **Date:** 2023-04-13
- **CVE:** CVE-2023-2019
- **CVSS:** 5.3
- **CVSS Vector:** AV:L/AC:H/PR:H/UI:N/S:C/C:N/I:N/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Lucas Leong (@_wmliang_) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-442/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of Linux Kernel. An attacker must first obtain the ability to execute high-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the scheduling of events. The issue results from the improper management of a reference count. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://git.kernel.org/pub/scm/linux/kernel/git/netdev/net.git/commit/?id=180a6a3ee60a

## Disclosure Timeline

- 2022-07-19 - Vulnerability reported to vendor
- 2023-04-13 - Coordinated public release of advisory
