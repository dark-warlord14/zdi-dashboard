# ZDI-19-569: Apple macOS AMDRadeonX4000_AMDAccelResource Integer Overflow Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-569
- **ZDI-CAN:** ZDI-CAN-8288
- **Date:** 2019-06-13
- **CVE:** CVE-2019-8519
- **CVSS:** 7.1
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Lilang Wu and Moony Li of TrendMicro Mobile Security Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-569/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on vulnerable installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of the AMDRadeonX4000_AMDAccelResource method. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before reading from memory. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges in the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT209600

## Disclosure Timeline

- 2019-03-08 - Vulnerability reported to vendor
- 2019-06-13 - Coordinated public release of advisory
