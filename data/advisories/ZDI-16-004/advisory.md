# ZDI-16-004: (0Day) Proface GP-Pro EX Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-004
- **ZDI-CAN:** ZDI-CAN-2946
- **Date:** 2016-01-08
- **CVE:** N/A
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Proface
- **Affected Products:** GP-Pro EX
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-004/
## Vulnerability Details

This vulnerability allows remote attackers to disclose information on vulnerable installations of Proface GP-Pro EX. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within BeginPreRead processing. When handling malformed 0x7f77 type fields, it is possible for an attacker to force an out-of-bounds read. An attacker can leverage this vulnerability to disclose arbitrary memory.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 06/25/2015 - ZDI disclosed 4 cases to ICS-CERT 06/25/2015 - ICS-CERT acknowledged and provided the ZDI an ICS-VU# 10/03/2015 - ZDI asked for an update from ICS-CERT and reminded of the 10/23/2015 due date, asking if a short extension was needed There was no reply but ZDI granted an extension for the cases. 12/09/2015 - ZDI wrote to ICS-CERT to ask the status and notify of the intent to 0-day the reports at EOY -- Mitigation: Given the stated purpose of Proface GP-Pro, and the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application to trusted files. -- Vendor Response Link: http://www.schneider-electric.com/ww/en/download/document/SEVD-2016-074-01

## Disclosure Timeline

- 2015-06-25 - Vulnerability reported to vendor
- 2016-01-08 - Coordinated public release of advisory
