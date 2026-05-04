# ZDI-07-027: Microsoft Internet Explorer Table Column Deletion Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-07-027
- **ZDI-CAN:** ZDI-CAN-098
- **Date:** 2007-05-08
- **CVE:** CVE-2007-0944
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer 6
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-027/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists in the CTableCol::OnPropertyChange() method. When a named table row in HTML contains a named table column, then calls the deleteCell() JavaScript method, any property of the table column, existing or not, accessed after the deletion takes place will trigger an exploitable memory corruption.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/ms07-027.mspx

## Disclosure Timeline

- 2006-10-03 - Vulnerability reported to vendor
- 2007-05-08 - Coordinated public release of advisory
