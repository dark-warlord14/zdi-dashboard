# ZDI-06-034: Microsoft Word Malformed Chart Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-034
- **ZDI-CAN:** ZDI-CAN-061
- **Date:** 2006-10-10
- **CVE:** CVE-2006-3650
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Word
- **Credit:** Arnaud Dovi 'class101' http://heapoverflow.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-034/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Microsoft Office. Exploitation requires that the attacker coerce the target user into opening a malicious .XLS file. The specific flaw exists during the processing of malformed charts embedded within a Word document. Upon closing the document, certain pointers are corrupted with data direclty from the file. A later dereference of these corrupted pointers can result in code execution.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/Bulletin/MS06-062.mspx

## Disclosure Timeline

- 2006-06-14 - Vulnerability reported to vendor
- 2006-10-10 - Coordinated public release of advisory
