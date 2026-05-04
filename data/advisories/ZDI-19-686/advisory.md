# ZDI-19-686: Apple macOS AMDRadeonX4000_AMDAccelResource initialize Out-Of-Bounds Read Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-686
- **ZDI-CAN:** ZDI-CAN-8536
- **Date:** 2019-07-24
- **CVE:** CVE-2019-8692
- **CVSS:** 4.7
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Lilang Wu and Moony Li of TrendMicro Mobile Security Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-686/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Apple MacOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the initialize method of the AMDRadeonX4000_AMDAccelSharedUserClient class. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated data structure. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges to the level of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT210348

## Disclosure Timeline

- 2019-04-03 - Vulnerability reported to vendor
- 2019-07-24 - Coordinated public release of advisory
