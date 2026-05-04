# ZDI-24-1088: (0Day) Microsoft 3D Viewer GLB File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1088
- **ZDI-CAN:** ZDI-CAN-19051
- **Date:** 2024-08-06
- **CVE:** N/A
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** 3D Viewer
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1088/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Microsoft 3D Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of GLB files. Crafted data in a GLB file can trigger a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process at low integrity.

## Additional Details

09/30/22 – ZDI reported the vulnerability to the vendor. 10/06/22 – The vendor acknowledged the report. 12/28/22 – The vendor confirmed the report. 01/10/23 – The vendor states this doesn’t meet the bar for servicing. 10/06/23 – ZDI inquired about a fix for a similar case being related to this report. 02/05/24 – The vendor states this might be fixed and will verify. 02/28/24 – ZDI asked for an update. 08/05/24 – ZDI retested this vulnerability and determined that it’s still reproducible on the latest version and informed the vendor that we intend to publish this case as a zero-day advisory on 08/06/24. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application

## Disclosure Timeline

- 2022-09-30 - Vulnerability reported to vendor
- 2024-08-06 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
