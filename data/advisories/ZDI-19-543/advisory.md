# ZDI-19-543: Apple macOS AMDRadeonX4000_AMDSIGLContext Double Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-543
- **ZDI-CAN:** ZDI-CAN-8345
- **Date:** 2019-06-07
- **CVE:** CVE-2019-8635
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Lilang Wu and Moony Li of TrendMicro Mobile Security Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-543/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on affected installations of Apple MacOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within processing of sideband tokens in the AMDRadeonX4000_AMDSIGLContext class. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privileges to the level of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT210119

## Disclosure Timeline

- 2019-03-14 - Vulnerability reported to vendor
- 2019-06-07 - Coordinated public release of advisory
