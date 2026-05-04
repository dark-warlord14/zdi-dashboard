# ZDI-25-246: MedDream WEB DICOM Viewer Cleartext Transmission of Credentials Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-246
- **ZDI-CAN:** ZDI-CAN-25842
- **Date:** 2025-04-09
- **CVE:** CVE-2025-3480
- **CVSS:** 5.3
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** MedDream
- **Affected Products:** WEB DICOM Viewer
- **Credit:** Chizuru Toyama of TXOne Networks
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-246/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to disclose sensitive information on affected installations of MedDream WEB DICOM Viewer. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Web Portal. The issue results from the lack of encryption when transmitting credentials. An attacker can leverage this vulnerability to disclose transmitted credentials, leading to further compromise.

## Additional Details

Fixed in version 7.3.5.860

## Disclosure Timeline

- 2024-12-10 - Vulnerability reported to vendor
- 2025-04-09 - Coordinated public release of advisory
- 2025-04-22 - Advisory Updated
