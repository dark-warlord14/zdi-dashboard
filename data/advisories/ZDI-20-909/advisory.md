# ZDI-20-909: Apple Safari getAnimations Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-909
- **ZDI-CAN:** ZDI-CAN-10832
- **Date:** 2020-07-21
- **CVE:** CVE-2020-9894
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** 0011
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-909/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information code on affected installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the getAnimations method. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-gb/HT211292

## Disclosure Timeline

- 2020-04-30 - Vulnerability reported to vendor
- 2020-07-21 - Coordinated public release of advisory
