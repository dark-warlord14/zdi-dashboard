# ZDI-23-883: (Pwn2Own) Microsoft SharePoint GenerateProxyAssembly Code Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-883
- **ZDI-CAN:** ZDI-CAN-20749
- **Date:** 2023-06-16
- **CVE:** CVE-2023-24955
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** SharePoint
- **Credit:** Nguyễn Tiến Giang (@testanull) of STAR Labs SG Pte. Ltd.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-883/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft SharePoint. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the GenerateProxyAssembly method. The issue results from the lack of proper validation of a user-supplied string before using it to execute C# code. An attacker can leverage this vulnerability to execute code in the context of SharePoint farm service account.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-24954

## Disclosure Timeline

- 2023-03-30 - Vulnerability reported to vendor
- 2023-06-16 - Coordinated public release of advisory
- 2023-06-20 - Advisory Updated
