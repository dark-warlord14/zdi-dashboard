# ZDI-22-1462: (Pwn2Own) Linux Kernel io_uring Improper Update of Reference Count Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1462
- **ZDI-CAN:** ZDI-CAN-17428
- **Date:** 2022-10-21
- **CVE:** CVE-2022-2602
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Billy Jheng Bing-Jhong (https://twitter.com/st424204) of STAR Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1462/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Linux Kernel. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the io_uring API. The issue results from the improper management of a reference count. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://ubuntu.com/security/CVE-2022-2602

## Disclosure Timeline

- 2022-05-25 - Vulnerability reported to vendor
- 2022-10-21 - Coordinated public release of advisory
