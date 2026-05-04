# ZDI-18-1083: Apple Safari Array Concat Uninitialized Buffer Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1083
- **ZDI-CAN:** ZDI-CAN-6666
- **Date:** 2018-09-24
- **CVE:** CVE-2018-4358
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** @phoenhex team (@bkth_ @5aelo @_niklasb)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1083/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of Arrays. By performing actions in JavaScript, an attacker can trigger access to memory prior to initialization. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT209109

## Disclosure Timeline

- 2018-07-19 - Vulnerability reported to vendor
- 2018-09-24 - Coordinated public release of advisory
- 2018-09-24 - Advisory Updated
