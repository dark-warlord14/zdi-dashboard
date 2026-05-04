# ZDI-24-1274: (0Day) FastStone Image Viewer TGA File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1274
- **ZDI-CAN:** ZDI-CAN-25140
- **Date:** 2024-09-23
- **CVE:** CVE-2024-9113
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** FastStone
- **Affected Products:** Image Viewer
- **Credit:** Zeze with TeamT5
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1274/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of FastStone Image Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of TGA files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

08/22/24 – ZDI requested the vendor’s PSIRT contacts 08/30/24 – ZDI asked for updates 09/11/24 – ZDI notified the vendor of the intention to publish the case as 0-day advisory

## Disclosure Timeline

- 2024-09-12 - Vulnerability reported to vendor
- 2024-09-23 - Coordinated public release of advisory
- 2024-09-23 - Advisory Updated
