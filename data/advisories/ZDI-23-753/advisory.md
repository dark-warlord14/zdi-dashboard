# ZDI-23-753: (0Day) Microsoft 3D Viewer PLY File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-753
- **ZDI-CAN:** ZDI-CAN-19052
- **Date:** 2023-05-31
- **CVE:** N/A
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** 3D Viewer
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-753/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Microsoft 3D Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PLY files. Crafted data in a PLY file can trigger a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process at low integrity.

## Additional Details

09/30/22 – ZDI reported the vulnerability to the vendor. 10/07/22 – The vendor acknowledged the report. 12/30/22 – The vendor stated that this vulnerability does not pose an immediate threat, but they shared their findings with the development team for a fix in a later build. 03/10/23 – ZDI informed the vendor that this case will be published as a zero-day advisory on 3/14/23. 03/13/23 – The vendor informed the ZDI that they patched numerous cases that were scheduled to be published as zero-day advisories. 05/24/23 – The ZDI rescheduled the publication date to 05/31/23. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2022-09-30 - Vulnerability reported to vendor
- 2023-05-31 - Coordinated public release of advisory
- 2023-05-31 - Advisory Updated
