# ZDI-19-539: Apple macOS AMDRadeonX4000_AMDSIGLContext discard_StretchTex2Tex Double Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-539
- **ZDI-CAN:** ZDI-CAN-8547
- **Date:** 2019-05-30
- **CVE:** CVE-2019-8635
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Lilang Wu and Moony Li of TrendMicro Mobile Security Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-539/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the discard_StretchTex2Tex method of the AMDRadeonX4000_AMDSIGLContext class. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated data structure. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges to the level of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT210119

## Disclosure Timeline

- 2019-04-08 - Vulnerability reported to vendor
- 2019-05-30 - Coordinated public release of advisory
