# ZDI-19-289: Apple macOS AMDRadeonX4000 Out-Of-Bounds Read Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-289
- **ZDI-CAN:** ZDI-CAN-7604
- **Date:** 2019-03-26
- **CVE:** CVE-2019-8519
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** juwei lin(@panicaII), junzhi lu of TrendMicro Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-289/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on vulnerable installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the AMDRadeonX4000 kernel extension. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges in the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT209600

## Disclosure Timeline

- 2018-11-27 - Vulnerability reported to vendor
- 2019-03-26 - Coordinated public release of advisory
