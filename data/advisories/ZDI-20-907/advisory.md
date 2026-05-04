# ZDI-20-907: Apple Safari RenderWidget Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-907
- **ZDI-CAN:** ZDI-CAN-10111
- **Date:** 2020-07-21
- **CVE:** CVE-2020-9893
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** 0011
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-907/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the RenderWidget class. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-gb/HT211292

## Disclosure Timeline

- 2020-04-14 - Vulnerability reported to vendor
- 2020-07-21 - Coordinated public release of advisory
