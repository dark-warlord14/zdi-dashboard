# ZDI-24-1095: (0Day) Microsoft Office Visio DXF File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1095
- **ZDI-CAN:** ZDI-CAN-22326
- **Date:** 2024-08-06
- **CVE:** N/A
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Visio
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1095/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Microsoft Office Visio. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DXF files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated object. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

10/12/23 – ZDI reported the vulnerability to the vendor. 10/14/23 – The vendor acknowledged the report. 11/03/23 – The vendor states this case doesn’t meet the bar for immediate servicing. 05/06/24 – ZDI asked for an update. 05/16/24 – The vendor states this might be fixed and will verify. 08/05/24 – ZDI retested this vulnerability and determined that it’s still reproducible on the latest version and informed the vendor that we intend to publish this case as a zero-day advisory on 08/06/24. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application

## Disclosure Timeline

- 2023-10-12 - Vulnerability reported to vendor
- 2024-08-06 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
