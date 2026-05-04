# ZDI-19-475: Microsoft Windows Mail HTML Line Breaking Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-475
- **ZDI-CAN:** ZDI-CAN-8423
- **Date:** 2019-05-15
- **CVE:** CVE-2019-0953
- **CVSS:** 7.7
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:L
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-475/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. Authentication is not required to exploit this vulnerability. The specific flaw exists within the logic that implements automatic line breaks when displaying HTML content in the Windows Mail app. By manipulating a document's elements, an attacker can trigger a read past the end of an allocated array. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-0953

## Disclosure Timeline

- 2019-04-19 - Vulnerability reported to vendor
- 2019-05-15 - Coordinated public release of advisory
