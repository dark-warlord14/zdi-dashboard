# ZDI-22-809: Microsoft Excel XLS File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-809
- **ZDI-CAN:** ZDI-CAN-16249
- **Date:** 2022-06-01
- **CVE:** CVE-2022-26901
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Excel
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-809/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Excel. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of XLS files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-26901

## Disclosure Timeline

- 2022-01-26 - Vulnerability reported to vendor
- 2022-06-01 - Coordinated public release of advisory
