# ZDI-19-816: Microsoft Azure DevOps Server Markdown Indexing Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-816
- **ZDI-CAN:** ZDI-CAN-9120
- **Date:** 2019-09-10
- **CVE:** CVE-2019-1306
- **CVSS:** 8.3
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:L
- **Affected Vendors:** Microsoft
- **Affected Products:** Azure
- **Credit:** Mikhail Shcherbakov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-816/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Azure DevOps Server. Authentication is required to exploit this vulnerability. The specific flaw exists within the processing of markdown files during indexing of wiki content. A crafted document uploaded to a wiki can trigger the deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of LOCAL SERVICE.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1306

## Disclosure Timeline

- 2019-08-08 - Vulnerability reported to vendor
- 2019-09-10 - Coordinated public release of advisory
