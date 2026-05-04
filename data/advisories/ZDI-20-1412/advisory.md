# ZDI-20-1412: Microsoft SharePoint Site Import Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1412
- **ZDI-CAN:** ZDI-CAN-11873
- **Date:** 2020-12-09
- **CVE:** CVE-2020-17121
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** SharePoint
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1412/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft SharePoint. Authentication is required to exploit this vulnerability. The specific flaw exists within the ImportWeb function. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2020-17121

## Disclosure Timeline

- 2020-09-08 - Vulnerability reported to vendor
- 2020-12-09 - Coordinated public release of advisory
