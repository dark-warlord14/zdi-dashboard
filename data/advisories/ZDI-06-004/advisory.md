# ZDI-06-004: Microsoft Excel File Format Parsing Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-004
- **ZDI-CAN:** ZDI-CAN-024
- **Date:** 2006-03-14
- **CVE:** CVE-2006-0028
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Excel
- **Credit:** Arnaud Dovi aka 'class101', http://heapoverflow.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-004/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office. Exploitation requires that the attacker coerce the target into opening a malicious .XLS file. The specific flaw exists within the parsing of the BIFF file format used by Microsoft Excel. During the processing of malformed BOOLERR records, user-supplied data may be insecurely referenced thereby leading to the eventual execution of arbitrary code.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/ms06-012.mspx

## Disclosure Timeline

- 2006-01-24 - Vulnerability reported to vendor
- 2006-03-14 - Coordinated public release of advisory
