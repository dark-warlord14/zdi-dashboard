# ZDI-17-191: Apple Safari ElementData Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-191
- **ZDI-CAN:** ZDI-CAN-4454
- **Date:** 2017-03-28
- **CVE:** CVE-2017-2481
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** 0011
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-191/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of ElementData objects. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to achieve remote code execution under the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/kb/HT201222

## Disclosure Timeline

- 2017-02-09 - Vulnerability reported to vendor
- 2017-03-28 - Coordinated public release of advisory
