# ZDI-07-026: Microsoft Excel BIFF File Format Named Graph Record Parsing Stack Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-026
- **ZDI-CAN:** ZDI-CAN-131
- **Date:** 2007-05-08
- **CVE:** CVE-2007-0215
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft, Microsoft, Microsoft
- **Affected Products:** Office Excel 2000, Office Excel 2002, Office Excel 2003
- **Credit:** Manuel Santamarina Suarez
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-026/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office Excel. Exploitation requires that the attacker coerce the target into opening a malicious .XLS file. The specific flaw exists within the parsing of the BIFF file format used by Microsoft Excel. During the processing of a malformed Named Graph record, user-supplied data may be copied to the stack unchecked thereby leading to an exploitable stack-based buffer overflow.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/ms07-023.mspx

## Disclosure Timeline

- 2006-11-16 - Vulnerability reported to vendor
- 2007-05-08 - Coordinated public release of advisory
