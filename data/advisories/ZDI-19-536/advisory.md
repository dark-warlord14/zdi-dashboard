# ZDI-19-536: Apple Safari HTMLFormElement Improper Validation of Array Index Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-536
- **ZDI-CAN:** ZDI-CAN-8106
- **Date:** 2019-05-30
- **CVE:** CVE-2019-8587
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:L/I:L/A:L
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** G. Geshev
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-536/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within HTMLFormElement objects. The issue results from the lack of proper validation of user-supplied data, which can result in memory access past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT210119

## Disclosure Timeline

- 2019-03-04 - Vulnerability reported to vendor
- 2019-05-30 - Coordinated public release of advisory
