# ZDI-21-969: Microsoft Excel XLS File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-969
- **ZDI-CAN:** ZDI-CAN-13508
- **Date:** 2021-08-11
- **CVE:** CVE-2021-34501
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Excel
- **Credit:** 14
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-969/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Excel. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of CONTINUEFRT12 records within XLS files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34501

## Disclosure Timeline

- 2021-04-16 - Vulnerability reported to vendor
- 2021-08-11 - Coordinated public release of advisory
