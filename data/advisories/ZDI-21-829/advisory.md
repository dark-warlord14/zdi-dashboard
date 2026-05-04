# ZDI-21-829: Microsoft SharePoint CabUtility ExtractCab Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-829
- **ZDI-CAN:** ZDI-CAN-13584
- **Date:** 2021-07-19
- **CVE:** CVE-2021-34468
- **CVSS:** 7.1
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** SharePoint
- **Credit:** Steven Seeley (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-829/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Microsoft SharePoint. User interaction is required to exploit this vulnerability. The specific flaw exists within the parsing of CAB files. When handling filenames specified within a CAB file, the process does not properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the service account.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/en-us/vulnerability/CVE-2021-34468

## Disclosure Timeline

- 2021-05-07 - Vulnerability reported to vendor
- 2021-07-19 - Coordinated public release of advisory
