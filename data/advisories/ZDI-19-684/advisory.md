# ZDI-19-684: Apple Safari InlineFlowBox Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-684
- **ZDI-CAN:** ZDI-CAN-8439
- **Date:** 2019-07-24
- **CVE:** CVE-2019-8681
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:L/I:L/A:L
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** G. Geshev
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-684/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the deleteLine method. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT210348

## Disclosure Timeline

- 2019-05-02 - Vulnerability reported to vendor
- 2019-07-24 - Coordinated public release of advisory
