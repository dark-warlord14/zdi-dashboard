# ZDI-22-1605: (Pwn2Own) Microsoft Teams WebView Incorrect Privilege Assignment Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1605
- **ZDI-CAN:** ZDI-CAN-17393
- **Date:** 2022-11-21
- **CVE:** N/A
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Teams
- **Credit:** Hector "p3rr0" Peralta @hperalta89
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1605/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Teams. No user interaction is required if the attacker and target are in the same Teams organization and are both participants in a meeting. The specific flaw exists within handling of WebViews. The issue results from the creation of a WebView with inappropriate privileges. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Fixed on August 31, 2022 https://msrc.microsoft.com/update-guide/acknowledgement/online

## Disclosure Timeline

- 2022-05-26 - Vulnerability reported to vendor
- 2022-11-21 - Coordinated public release of advisory
