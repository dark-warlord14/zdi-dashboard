# ZDI-24-1018: (Pwn2Own) Linux Kernel io_uring Buffer List Race Condition Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1018
- **ZDI-CAN:** ZDI-CAN-23851
- **Date:** 2024-07-29
- **CVE:** CVE-2024-35880
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Linux
- **Affected Products:** Kernel
- **Credit:** Billy Jheng Bing-Jhong, Đỗ Minh Tuấn, Muhammad Alifa Ramdhan
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1018/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Linux Kernel. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of the io_uring buffer list. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Linux has issued an update to correct this vulnerability. More details can be found at: https://lore.kernel.org/linux-cve-announce/2024051944-CVE-2024-35880-6ffb@gregkh/#r

## Disclosure Timeline

- 2024-04-02 - Vulnerability reported to vendor
- 2024-07-29 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
