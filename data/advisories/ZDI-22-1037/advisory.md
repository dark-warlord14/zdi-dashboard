# ZDI-22-1037: NetBSD Kernel getkerninfo System Call Uninitialized Memory Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1037
- **ZDI-CAN:** ZDI-CAN-14809
- **Date:** 2022-08-02
- **CVE:** N/A
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** NetBSD
- **Affected Products:** Kernel
- **Credit:** Reno Robert of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1037/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of NetBSD Kernel. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the stat system call. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

NetBSD has issued an update to correct this vulnerability. More details can be found at: https://www.mail-archive.com/source-changes-d@netbsd.org/msg28615.html

## Disclosure Timeline

- 2022-01-19 - Vulnerability reported to vendor
- 2022-08-02 - Coordinated public release of advisory
