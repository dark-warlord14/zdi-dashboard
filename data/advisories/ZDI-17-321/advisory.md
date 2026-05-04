# ZDI-17-321: (Pwn2Own) Apple Safari String replace Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-321
- **ZDI-CAN:** ZDI-CAN-4578
- **Date:** 2017-05-04
- **CVE:** CVE-2017-2491
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Samuel Groß and Niklas Baumstark
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-321/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the String.replace method. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT207617

## Disclosure Timeline

- 2017-03-17 - Vulnerability reported to vendor
- 2017-05-04 - Coordinated public release of advisory
