# ZDI-11-281: Microsoft Office Graph DataFormat Signed Index Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-281
- **ZDI-CAN:** ZDI-CAN-1251
- **Date:** 2011-10-13
- **CVE:** CVE-2011-1990
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Excel
- **Credit:** Omair
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-281/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office 2007. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of a record inside a Microsoft Office Excel or PowerPoint document. When parsing a signed field from this structure, the application will use the field to seek into an array of objects. Due to this unbounded index, an attacker can cause an element outside the array to be treated as a different type. This type of corruption can lead to code execution under the context of the application.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://technet.microsoft.com/en-us/security/bulletin/ms11-072

## Disclosure Timeline

- 2011-06-01 - Vulnerability reported to vendor
- 2011-10-13 - Coordinated public release of advisory
