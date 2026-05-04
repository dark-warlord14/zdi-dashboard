# ZDI-25-950: 7-Zip ZIP File Parsing Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-950
- **ZDI-CAN:** ZDI-CAN-26743
- **Date:** 2025-10-07
- **CVE:** CVE-2025-11002
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** 7-Zip
- **Affected Products:** 7-Zip
- **Credit:** Ryota Shiga (GMO Flatt Security Inc.) with takumi-san.ai
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-950/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of 7-Zip. Interaction with this product is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the handling of symbolic links in ZIP files. Crafted data in a ZIP file can cause the process to traverse to unintended directories. An attacker can leverage this vulnerability to execute code in the context of a service account.

## Additional Details

Fixed in 7-Zip 25.00

## Disclosure Timeline

- 2025-05-02 - Vulnerability reported to vendor
- 2025-10-07 - Coordinated public release of advisory
- 2025-10-07 - Advisory Updated
