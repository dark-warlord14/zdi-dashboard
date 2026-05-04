# ZDI-25-048: Apple WebKit WebCore ContainerNode Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-048
- **ZDI-CAN:** ZDI-CAN-24012
- **Date:** 2025-01-20
- **CVE:** CVE-2024-27856
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** WebKit
- **Credit:** wac
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-048/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apple WebKit. User interaction is required to exploit this vulnerability. The specific flaw exists within the processing of Text objects. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/120903

## Disclosure Timeline

- 2024-05-09 - Vulnerability reported to vendor
- 2025-01-20 - Coordinated public release of advisory
- 2025-03-06 - Advisory Updated
