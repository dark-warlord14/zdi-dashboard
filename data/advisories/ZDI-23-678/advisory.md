# ZDI-23-678: Delta Electronics InfraSuite Device Master CtrlLayerNWCmd_ReportFileOperation Directory Traversal Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-678
- **ZDI-CAN:** ZDI-CAN-19280
- **Date:** 2023-05-17
- **CVE:** CVE-2023-1134
- **CVSS:** 7.1
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:H
- **Affected Vendors:** Delta Electronics
- **Affected Products:** InfraSuite Device Master
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-678/
## Vulnerability Details

This vulnerability allows remote attackers to delete arbitrary files on affected installations of Delta Electronics InfraSuite Device Master. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the CtrlLayerNWCmd_ReportFileOperation function. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to delete files in the context of an administrator.

## Additional Details

Delta Electronics has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-23-080-02

## Disclosure Timeline

- 2022-10-31 - Vulnerability reported to vendor
- 2023-05-17 - Coordinated public release of advisory
