# ZDI-20-1390: Apple Safari RenderObject Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1390
- **ZDI-CAN:** ZDI-CAN-11125
- **Date:** 2020-12-03
- **CVE:** CVE-2020-9947
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** cc
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1390/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of RenderObject objects. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT211845

## Disclosure Timeline

- 2020-06-19 - Vulnerability reported to vendor
- 2020-12-03 - Coordinated public release of advisory
