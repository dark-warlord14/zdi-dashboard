# ZDI-21-761: Apple WebKit KeyframeEffect Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-761
- **ZDI-CAN:** ZDI-CAN-12579
- **Date:** 2021-06-25
- **CVE:** CVE-2021-30749
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** WebKit
- **Credit:** mipu94 of SEFCOM lab, ASU.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-761/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple WebKit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the KeyframeEffect class. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/HT212529

## Disclosure Timeline

- 2021-02-12 - Vulnerability reported to vendor
- 2021-06-25 - Coordinated public release of advisory
