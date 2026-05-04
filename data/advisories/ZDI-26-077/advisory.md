# ZDI-26-077: GFI Archiver MArc.Store Missing Authorization Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-077
- **ZDI-CAN:** ZDI-CAN-28597
- **Date:** 2026-02-12
- **CVE:** CVE-2026-2039
- **CVSS:** 7.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L
- **Affected Vendors:** GFI
- **Affected Products:** Archiver
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-077/
## Vulnerability Details

This vulnerability allows remote attackers to bypass authentication on affected installations of GFI Archiver. Authentication is not required to exploit this vulnerability. The specific flaw exists within the configuration of the MArc.Store.Remoting.exe process, which listens on port 8018. The issue results from the lack of authorization prior to allowing access to functionality. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of SYSTEM.

## Additional Details

Fixed in Version 15.11 https://gfi.ai/products-and-solutions/network-security-solutions/archiver/resources/documentation/product-releases

## Disclosure Timeline

- 2025-11-19 - Vulnerability reported to vendor
- 2026-02-12 - Coordinated public release of advisory
- 2026-02-12 - Advisory Updated
