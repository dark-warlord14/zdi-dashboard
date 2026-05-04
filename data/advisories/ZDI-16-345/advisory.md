# ZDI-16-345: (Pwn2Own) Apple OS X IntelAccelerator Out-Of-Bounds Indexing Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-345
- **ZDI-CAN:** ZDI-CAN-3620
- **Date:** 2016-05-19
- **CVE:** CVE-2016-1815
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** Liang Chen and Qidan He of KeenLab Tencent
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-345/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Apple OS X. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the IntelAccelerator kext. The issue lies in the blit3d_submit_commands function, which fails to properly validate the bounds of a vector. An attacker can leverage this vulnerability to elevate privileges and execute code within the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT206567

## Disclosure Timeline

- 2016-03-16 - Vulnerability reported to vendor
- 2016-05-19 - Coordinated public release of advisory
