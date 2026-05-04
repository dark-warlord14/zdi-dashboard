# ZDI-11-346: Microsoft Office 2007 Office Art Shape Record Hierarchy Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-346
- **ZDI-CAN:** ZDI-CAN-1280
- **Date:** 2011-12-13
- **CVE:** CVE-2011-3413
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft, Microsoft
- **Affected Products:** Office Excel, Office PowerPoint
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-346/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office 2007. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within how the application processes a shape record hierarchy. Due to the application not properly checking the types of elements within containers, the application will incorrectly modify a property of the object. This modification can be used to cause memory corruption of the type which can lead to code execution under the context of the application.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://technet.microsoft.com/en-us/security/bulletin/MS11-094 Microsoft has issued an update to correct this vulnerability. More details can be found at: http://technet.microsoft.com/en-us/security/bulletin/MS11-094

## Disclosure Timeline

- 2011-06-29 - Vulnerability reported to vendor
- 2011-12-13 - Coordinated public release of advisory
