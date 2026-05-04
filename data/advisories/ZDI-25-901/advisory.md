# ZDI-25-901: Apple Safari IPC Connection Invalidation Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-901
- **ZDI-CAN:** ZDI-CAN-27586
- **Date:** 2025-09-18
- **CVE:** CVE-2025-43368
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Pawel Wylecial of REDTEAM.PL
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-901/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of IPC connection invalidation. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-ca/125113

## Disclosure Timeline

- 2025-07-22 - Vulnerability reported to vendor
- 2025-09-18 - Coordinated public release of advisory
- 2025-09-18 - Advisory Updated
