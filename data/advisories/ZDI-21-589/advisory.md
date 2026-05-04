# ZDI-21-589: (Pwn2Own) Canonical Ubuntu io_uring Integer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-589
- **ZDI-CAN:** ZDI-CAN-13546
- **Date:** 2021-05-13
- **CVE:** CVE-2021-3491
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Canonical
- **Affected Products:** Ubuntu
- **Credit:** Billy Jheng Bing-Jhong (@st424204) of STAR Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-589/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Canonical Ubuntu. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of buffers in io_uring. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before accessing memory. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Canonical has issued an update to correct this vulnerability. More details can be found at: https://www.openwall.com/lists/oss-security/2021/05/11/13

## Disclosure Timeline

- 2021-04-22 - Vulnerability reported to vendor
- 2021-05-13 - Coordinated public release of advisory
