# ZDI-24-198: PDF-XChange Editor Updater Improper Certificate Validation Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-198
- **ZDI-CAN:** ZDI-CAN-22224
- **Date:** 2024-02-23
- **CVE:** CVE-2024-27323
- **CVSS:** 7.5
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** PDF-XChange
- **Affected Products:** PDF-XChange Editor
- **Credit:** Bobby Gould and Anthony Fuller of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-198/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of PDF-XChange Editor. User interaction is not required to exploit this vulnerability. The specific flaw exists within the update functionality. The issue results from the lack of proper validation of the certificate presented by the server. An attacker can leverage this vulnerability to execute code in the context of the current user.

## Additional Details

fixed in version 10.1.2.382: https://www.pdf-xchange.com/support/security-bulletins.html

## Disclosure Timeline

- 2023-09-27 - Vulnerability reported to vendor
- 2024-02-23 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
