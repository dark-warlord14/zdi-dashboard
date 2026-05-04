# ZDI-25-030: Microsoft Office Word DOCX File Parsing Uninitialized Pointer Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-030
- **ZDI-CAN:** ZDI-CAN-25187
- **Date:** 2025-01-15
- **CVE:** CVE-2025-21363
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Word
- **Credit:** Jmini, Rotiple, D4m0n
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-030/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Office Word. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DOCX files. The issue results from the lack of proper initialization of a pointer prior to accessing it. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21363

## Disclosure Timeline

- 2024-10-31 - Vulnerability reported to vendor
- 2025-01-15 - Coordinated public release of advisory
- 2025-01-15 - Advisory Updated
