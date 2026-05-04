# ZDI-22-865: SAP 3D Visual Enterprise Viewer CGM File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-865
- **ZDI-CAN:** ZDI-CAN-16279
- **Date:** 2022-06-16
- **CVE:** CVE-2022-26106
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** SAP
- **Affected Products:** 3D Visual Enterprise Viewer
- **Credit:** insu of Diffense
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-865/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of SAP 3D Visual Enterprise Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of CGM files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

SAP has issued an update to correct this vulnerability. More details can be found at: https://dam.sap.com/mac/app/e/pdf/preview/embed/ucQrx6G?ltr=a&rc=10

## Disclosure Timeline

- 2022-02-02 - Vulnerability reported to vendor
- 2022-06-16 - Coordinated public release of advisory
