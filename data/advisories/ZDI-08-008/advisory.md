# ZDI-08-008: Microsoft Excel BIFF File Format Cell Record Parsing Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-008
- **ZDI-CAN:** ZDI-CAN-195
- **Date:** 2008-03-11
- **CVE:** CVE-2008-0113
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Excel Viewer
- **Credit:** Arnaud Dovi - ad@heapoverflow.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-008/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office. Exploitation requires that the attacker coerce the target into opening a malicious .XLS file. The specific flaw exists within the parsing of malformed cell comments. When Excel encounters a malformed record it attempts to rebuild the broken meta-data. A flaw in this rebuilding process allows the user to specify critical data offsets eventually leading to code execution under the logged in users credentials.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/Bulletin/MS08-016.mspx

## Disclosure Timeline

- 2007-05-22 - Vulnerability reported to vendor
- 2008-03-11 - Coordinated public release of advisory
