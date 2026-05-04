# ZDI-11-125: Microsoft Office PowerPoint PersistDirectoryEntry Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-125
- **ZDI-CAN:** ZDI-CAN-901
- **Date:** 2011-04-12
- **CVE:** CVE-2011-0656
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Office PowerPoint
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-125/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office PowerPoint. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within how the application handles an exception within the PersistDirectoryEntry records when loading a presentation. When an entry points to a container containing a Slide with a malformed record, the application will raise an exception during the loading of the record. Afterward the application will use a method off of this malformed object which can lead to code execution under the context of the application.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/Bulletin/MS11-022.mspx

## Disclosure Timeline

- 2010-09-14 - Vulnerability reported to vendor
- 2011-04-12 - Coordinated public release of advisory
