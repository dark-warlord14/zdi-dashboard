# ZDI-20-672: (Pwn2Own) Apple Safari In Operator JIT Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-672
- **ZDI-CAN:** ZDI-CAN-10773
- **Date:** 2020-05-27
- **CVE:** CVE-2020-9850
- **CVSS:** 7.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** @jinmo123, @setuid0x0_, and @insu_yun_en of @SSLab_Gatech
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-672/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of the HasIndexedProperty DFG node. By performing actions in JavaScript, an attacker can trigger a type confusion condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

https://support.apple.com/en-gb/HT211177

## Disclosure Timeline

- 2020-03-26 - Vulnerability reported to vendor
- 2020-05-27 - Coordinated public release of advisory
