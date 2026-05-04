# ZDI-20-680: (Pwn2Own) Apple macOS Core Virtual Machine Service Heap-based Buffer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-680
- **ZDI-CAN:** ZDI-CAN-10775
- **Date:** 2020-05-28
- **CVE:** CVE-2020-9856
- **CVSS:** 5.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** @jinmo123, @setuid0x0_, and @insu_yun_en of @SSLab_Gatech
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-680/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of Core Virtual Machine Service caches. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute code in the context of the kernel.

## Additional Details

https://support.apple.com/en-gb/HT211170

## Disclosure Timeline

- 2020-05-27 - Vulnerability reported to vendor
- 2020-05-28 - Coordinated public release of advisory
