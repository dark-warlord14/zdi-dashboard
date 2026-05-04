# ZDI-20-823: Apple macOS AudioToolboxCore CAF File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-823
- **ZDI-CAN:** ZDI-CAN-10579
- **Date:** 2020-07-09
- **CVE:** CVE-2020-9815
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Yu Zhou(@yuzhou6666)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-823/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apple macOS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the AudioToolboxCore module. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated data structure. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-gb/HT211170

## Disclosure Timeline

- 2020-03-18 - Vulnerability reported to vendor
- 2020-07-09 - Coordinated public release of advisory
