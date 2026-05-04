# ZDI-25-1010: Apple Safari JavaScriptCore DFG CSE Phase Graph Node Substitution Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1010
- **ZDI-CAN:** ZDI-CAN-27991
- **Date:** 2025-11-13
- **CVE:** CVE-2025-43457
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Hossein Lotfi (@hosselot) of Trend Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1010/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of graph node substitution in the DFG CSE phase of JavaScriptCore. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the browser process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-ca/125640

## Disclosure Timeline

- 2025-08-26 - Vulnerability reported to vendor
- 2025-11-13 - Coordinated public release of advisory
- 2025-11-13 - Advisory Updated
