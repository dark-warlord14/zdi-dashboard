# ZDI-09-082: Microsoft Office Excel PivotTable Cache Record Parsing Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-082
- **ZDI-CAN:** ZDI-CAN-567
- **Date:** 2009-11-10
- **CVE:** CVE-2009-3127
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Excel
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-082/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office Excel. User interaction is required to exploit this vulnerability in that the target must open a malicious document. The specific flaw exists when parsing a document containing a malformed PivotCache Stream. The application will utilize the iCache value of an SXVI record to seek into a list of objects. While setting an attribute of that particular object, the application will corrupt memory which can lead to code execution under the context of the currently logged in user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS09-067.mspx

## Disclosure Timeline

- 2009-08-20 - Vulnerability reported to vendor
- 2009-11-10 - Coordinated public release of advisory
