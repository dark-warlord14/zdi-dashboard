# ZDI-18-1363: Apple macOS watchevent Use-After-Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1363
- **ZDI-CAN:** ZDI-CAN-7310
- **Date:** 2018-12-10
- **CVE:** CVE-2018-4447
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** Juwei Lin(@panicaII) and Zhengyu Dong of TrendMicro Mobile Security Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1363/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of the watchevent system call. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this to escalate privileges in the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT209341

## Disclosure Timeline

- 2018-09-27 - Vulnerability reported to vendor
- 2018-12-10 - Coordinated public release of advisory
