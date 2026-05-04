# ZDI-17-240: (Pwn2Own) Linux Kernel XFRM Out-Of-Bounds Access Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-240
- **ZDI-CAN:** ZDI-CAN-4586
- **Date:** 2017-03-30
- **CVE:** CVE-2017-7184
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Linux
- **Affected Products:** Linux Kernel
- **Credit:** Chaitin Security Research Lab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-240/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of the Linux Kernel. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of xfrm states. The issue results from the lack of proper validation of user-supplied data, which can result in a memory access past the end of an allocated buffer. An attacker can leverage this vulnerability to elevate privileges and execute arbitrary code under the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://www.ubuntu.com/usn/usn-3251-1/

## Disclosure Timeline

- 2017-03-18 - Vulnerability reported to vendor
- 2017-03-30 - Coordinated public release of advisory
