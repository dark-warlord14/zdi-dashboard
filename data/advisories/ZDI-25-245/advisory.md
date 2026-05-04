# ZDI-25-245: MedDream PACS Server DICOM File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-245
- **ZDI-CAN:** ZDI-CAN-25827
- **Date:** 2025-04-09
- **CVE:** CVE-2025-3481
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** MedDream
- **Affected Products:** PACS Server
- **Credit:** Chizuru Toyama of TXOne Networks
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-245/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of MedDream PACS Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the parsing of DICOM files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Fixed in version 7.3.5.860

## Disclosure Timeline

- 2024-12-10 - Vulnerability reported to vendor
- 2025-04-09 - Coordinated public release of advisory
- 2025-04-22 - Advisory Updated
