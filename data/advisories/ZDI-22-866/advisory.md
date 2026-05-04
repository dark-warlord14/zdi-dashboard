# ZDI-22-866: SAP 3D Visual Enterprise Viewer U3D File Parsing Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-866
- **ZDI-CAN:** ZDI-CAN-16007
- **Date:** 2022-06-17
- **CVE:** CVE-2022-27655
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** SAP
- **Affected Products:** 3D Visual Enterprise Viewer
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-866/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of SAP 3D Visual Enterprise Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of U3D files. Crafted data in a U3D file can trigger a read past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

SAP has issued an update to correct this vulnerability. More details can be found at: https://dam.sap.com/mac/app/e/pdf/preview/embed/ucQrx6G?ltr=a&rc=10

## Disclosure Timeline

- 2021-11-18 - Vulnerability reported to vendor
- 2022-06-17 - Coordinated public release of advisory
