# ZDI-18-1364: Apple macOS AMDFramebuffer Integer Overflow Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1364
- **ZDI-CAN:** ZDI-CAN-7302
- **Date:** 2018-12-10
- **CVE:** CVE-2018-4462
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** Lilang Wu, Moony Li of TrendMicro Mobile Security Research Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1364/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on vulnerable installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of the getPixelInformationFromTiming method. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before reading from memory. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges in the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT209341

## Disclosure Timeline

- 2018-09-26 - Vulnerability reported to vendor
- 2018-12-10 - Coordinated public release of advisory
