# ZDI-06-033: Microsoft Office Excel File Format DATETIME Record Parsing Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-033
- **ZDI-CAN:** ZDI-CAN-059
- **Date:** 2006-10-10
- **CVE:** CVE-2006-2387
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Excel
- **Credit:** Manuel Santamarina Suarez
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-033/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office. Exploitation requires that the attacker coerce the target user into opening a malicious .XLS file. The specific flaw exists within the parsing of the BIFF file format used by Microsoft Excel. During the processing of malformed DATETIME records, user-supplied data may be insecurely referenced thereby leading to the eventual execution of arbitrary code.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/Bulletin/MS06-059.mspx

## Disclosure Timeline

- 2006-06-15 - Vulnerability reported to vendor
- 2006-10-10 - Coordinated public release of advisory
