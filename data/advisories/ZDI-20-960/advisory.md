# ZDI-20-960: (Pwn2Own) Apple macOS kextload Time-Of-Check Time-Of-Use Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-960
- **ZDI-CAN:** ZDI-CAN-10778
- **Date:** 2020-08-10
- **CVE:** CVE-2020-9939
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** @SSLab_Gatech (@jinmo123, @setuid0x0_, and @insu_yun_en)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-960/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Apple macOS. An attacker must first obtain the ability to execute high-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of kernel extensions in kextload. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute code in the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT211289

## Disclosure Timeline

- 2020-07-23 - Vulnerability reported to vendor
- 2020-08-10 - Coordinated public release of advisory
- 2021-06-29 - Advisory Updated
