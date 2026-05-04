# ZDI-18-1332: Apple Safari RenderCounter Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1332
- **ZDI-CAN:** ZDI-CAN-6497
- **Date:** 2018-10-31
- **CVE:** CVE-2018-4376
- **CVSS:** 5.6
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** 010
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1332/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of CSS counters. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/kb/HT201222

## Disclosure Timeline

- 2018-06-28 - Vulnerability reported to vendor
- 2018-10-31 - Coordinated public release of advisory
