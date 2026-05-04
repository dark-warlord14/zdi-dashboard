# ZDI-22-1411: Microsoft Word DOCX File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1411
- **ZDI-CAN:** ZDI-CAN-17647
- **Date:** 2022-10-14
- **CVE:** CVE-2022-38048
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Word
- **Credit:** hades_kito
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1411/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Word. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DOCX files. Crafted data in a DOCX file can cause a pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-38048

## Disclosure Timeline

- 2022-07-11 - Vulnerability reported to vendor
- 2022-10-14 - Coordinated public release of advisory
