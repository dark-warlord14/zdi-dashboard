# ZDI-23-884: (Pwn2Own) Microsoft SharePoint userphoto Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-884
- **ZDI-CAN:** ZDI-CAN-20748
- **Date:** 2023-06-16
- **CVE:** CVE-2023-24954
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** SharePoint
- **Credit:** Nguyễn Tiến Giang (@testanull) of STAR Labs SG Pte. Ltd.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-884/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Microsoft SharePoint. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the userphoto endpoint. The issue results from the exposure of sensitive information. An attacker can leverage this vulnerability to disclose information in the context of the SharePoint server.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-24955

## Disclosure Timeline

- 2023-03-30 - Vulnerability reported to vendor
- 2023-06-16 - Coordinated public release of advisory
- 2023-06-20 - Advisory Updated
