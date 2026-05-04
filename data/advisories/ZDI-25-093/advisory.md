# ZDI-25-093: (Pwn2Own) Apple Safari Pointer Authentication Code Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-093
- **ZDI-CAN:** ZDI-CAN-26551
- **Date:** 2025-02-24
- **CVE:** CVE-2024-27834
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:L/I:L/A:L
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Manfred Paul (@_manfp)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-093/
## Vulnerability Details

This vulnerability allows remote attackers to bypass the Pointer Authentication Code protection mechanism on affected installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the libpas allocator. The protection mechanism does not properly protect the data pointers. An attacker can leverage this vulnerability to execute arbitrary code in the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-la/120896

## Disclosure Timeline

- 2025-02-12 - Vulnerability reported to vendor
- 2025-02-24 - Coordinated public release of advisory
- 2025-02-24 - Advisory Updated
