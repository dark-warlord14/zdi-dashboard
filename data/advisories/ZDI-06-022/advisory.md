# ZDI-06-022: Microsoft Office Excel File Rebuilding Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-022
- **ZDI-CAN:** ZDI-CAN-045
- **Date:** 2006-07-11
- **CVE:** CVE-2006-2388
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Excel
- **Credit:** Arnaud Dovi 'class101' http://heapoverflow.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-022/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office. Exploitation requires that the attacker coerce the target into opening a malicious .XLS file. The specific flaw exists within the rebuilding of malformed cell comments. When Excel encounters a malformed record it attempts to rebuild the broken meta-data. A flaw in this rebuilding process allows the user to specify critical data offsets eventually leading to code execution with the credentials of the current user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS06-037.mspx

## Disclosure Timeline

- 2006-06-15 - Vulnerability reported to vendor
- 2006-07-11 - Coordinated public release of advisory
