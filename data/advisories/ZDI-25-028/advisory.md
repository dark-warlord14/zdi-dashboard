# ZDI-25-028: Microsoft Office Word RTF File Parsing Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-028
- **ZDI-CAN:** ZDI-CAN-25188
- **Date:** 2025-01-15
- **CVE:** CVE-2025-21298
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Word
- **Credit:** Jmini, Rotiple, D4m0n
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-028/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Office Word. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of RTF files. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-21298

## Disclosure Timeline

- 2024-10-15 - Vulnerability reported to vendor
- 2025-01-15 - Coordinated public release of advisory
- 2025-01-15 - Advisory Updated
