# ZDI-19-864: Apple WebKit CSSAnimation Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-864
- **ZDI-CAN:** ZDI-CAN-8668
- **Date:** 2019-10-08
- **CVE:** CVE-2019-8707
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** WebKit
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-864/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple WebKit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of CSSAnimation objects. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT210637

## Disclosure Timeline

- 2019-06-21 - Vulnerability reported to vendor
- 2019-10-08 - Coordinated public release of advisory
