# ZDI-26-074: GFI Archiver MArc.Core Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-26-074
- **ZDI-CAN:** ZDI-CAN-27935
- **Date:** 2026-02-12
- **CVE:** CVE-2026-2037
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** GFI
- **Affected Products:** Archiver
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-26-074/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of GFI Archiver. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the configuration of the MArc.Core.Remoting.exe process, which listens on port 8017. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Fixed in Version 15.11 https://gfi.ai/products-and-solutions/network-security-solutions/archiver/resources/documentation/product-releases

## Disclosure Timeline

- 2025-11-19 - Vulnerability reported to vendor
- 2026-02-12 - Coordinated public release of advisory
- 2026-02-12 - Advisory Updated
