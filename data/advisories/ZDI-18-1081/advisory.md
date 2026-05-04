# ZDI-18-1081: Apple Safari performProxyCall Internal Object Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1081
- **ZDI-CAN:** ZDI-CAN-6361
- **Date:** 2018-09-24
- **CVE:** CVE-2018-4299
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Samuel Groβ (saelo)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1081/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of proxy calls. The issue lies in the lack of proper validation of an object prior to making a call. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT209109

## Disclosure Timeline

- 2018-06-14 - Vulnerability reported to vendor
- 2018-09-24 - Coordinated public release of advisory
- 2018-09-24 - Advisory Updated
