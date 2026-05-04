# ZDI-20-679: (Pwn2Own) Apple Safari Symbolic Link Arbitrary Application Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-679
- **ZDI-CAN:** ZDI-CAN-10774
- **Date:** 2020-05-28
- **CVE:** CVE-2020-9801
- **CVSS:** 5.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** @jinmo123, @setuid0x0_, and @insu_yun_en of @SSLab_Gatech
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-679/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Apple Safari. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of symbolic links. The issue results from the improper validation of symbolic links prior to performing operations on them. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute code in the context of the kernel.

## Additional Details

https://support.apple.com/en-gb/HT211177

## Disclosure Timeline

- 2020-05-27 - Vulnerability reported to vendor
- 2020-05-28 - Coordinated public release of advisory
