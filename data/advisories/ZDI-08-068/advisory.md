# ZDI-08-068: Microsoft Office Excel BIFF File Format Parsing Stack Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-068
- **ZDI-CAN:** ZDI-CAN-345
- **Date:** 2008-10-14
- **CVE:** CVE-2008-3471
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Excel
- **Credit:** wushi & ling of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-068/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office Excel. Exploitation requires that the victim to open the malformed BIFF (.xls) document. The specific flaw exists within the parsing of the BIFF file format used by Microsoft Excel. During the processing of a malformed record, user-supplied data is copied into a stack-based buffer using a size that is calculated using contents from the record.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS08-057.mspx

## Disclosure Timeline

- 2008-05-23 - Vulnerability reported to vendor
- 2008-10-14 - Coordinated public release of advisory
