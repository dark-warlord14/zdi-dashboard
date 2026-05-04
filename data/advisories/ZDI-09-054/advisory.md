# ZDI-09-054: Microsoft Office OWC10.Spreadsheet ActiveX msDataSourceObject() Heap Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-054
- **ZDI-CAN:** ZDI-CAN-175
- **Date:** 2009-08-11
- **CVE:** CVE-2009-1136
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft, Microsoft
- **Affected Products:** Office Word, Office Excel
- **Credit:** Peter Vreugdenhil
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-054/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Microsoft Office. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists during the processing of malicious parameters to the routine msDataSourceObject() and results in transfer of control to unallocated memory. This issue can be exploited to execute arbitrary code under the context of the currently logged in user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS09-043.mspx

## Disclosure Timeline

- 2007-03-19 - Vulnerability reported to vendor
- 2009-08-11 - Coordinated public release of advisory
