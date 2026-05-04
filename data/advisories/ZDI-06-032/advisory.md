# ZDI-06-032: Microsoft PowerPoint Malformed Slide Notes Rebuilding Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-032
- **ZDI-CAN:** ZDI-CAN-065
- **Date:** 2006-10-10
- **CVE:** CVE-2006-3435
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** File Format Vulnerability
- **Credit:** Arnaud Dovi aka 'class101', http://heapoverflow.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-032/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Microsoft Office. Exploitation requires that the attacker coerce the target user into opening a malicious .PPT file. The specific flaw exists during the parsing of a malformed slide notes field within the PowerPoint presentation. When PowerPoint attempts to rebuild the malformed section, a pointer calculation is made based on attacker controlled data from within the file. This pointer is later dereferenced and can lead to arbitrary code execution with the privileges of the user who opened the malicious file.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/Bulletin/MS06-058.mspx

## Disclosure Timeline

- 2006-06-14 - Vulnerability reported to vendor
- 2006-10-10 - Coordinated public release of advisory
