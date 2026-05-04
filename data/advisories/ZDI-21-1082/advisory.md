# ZDI-21-1082: Microsoft Word DOC File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1082
- **ZDI-CAN:** ZDI-CAN-13918
- **Date:** 2021-09-16
- **CVE:** CVE-2021-38656
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Word
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1082/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Word. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DOC files. Crafted data in a DOC file can cause a pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-38656

## Disclosure Timeline

- 2021-07-09 - Vulnerability reported to vendor
- 2021-09-16 - Coordinated public release of advisory
