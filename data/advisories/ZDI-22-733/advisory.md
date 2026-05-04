# ZDI-22-733: Microsoft Visual Studio DDS File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-733
- **ZDI-CAN:** ZDI-CAN-16189
- **Date:** 2022-05-10
- **CVE:** CVE-2022-29148
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Visual Studio
- **Credit:** ZhangYang
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-733/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Visual Studio. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DDS files. Crafted data in a DDS file can trigger an overflow of a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-29148

## Disclosure Timeline

- 2022-02-09 - Vulnerability reported to vendor
- 2022-05-10 - Coordinated public release of advisory
