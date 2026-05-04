# ZDI-08-048: Microsoft Excel COUNTRY Record Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-048
- **ZDI-CAN:** ZDI-CAN-307
- **Date:** 2008-08-12
- **CVE:** CVE-2008-3006
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Excel
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-048/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office Excel. Exploitation requires that the attacker coerce the target into opening a malicious .XLS file. The specific flaw exists within the parsing of the BIFF file format used by Microsoft Excel. During the processing of a malformed Country (0x8c) record, user-supplied data may be used in a memory copy operation resulting in memory corruption. If successfully exploited remote control of the affected system can be obtained under the credentials of the currently logged in user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS08-043.mspx

## Disclosure Timeline

- 2008-04-16 - Vulnerability reported to vendor
- 2008-08-12 - Coordinated public release of advisory
