# ZDI-22-1672: Microsoft Office Visio DWG File Parsing Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1672
- **ZDI-CAN:** ZDI-CAN-19048
- **Date:** 2022-12-15
- **CVE:** CVE-2022-44695
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Visio
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1672/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Microsoft Office Visio. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DWG files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-44695

## Disclosure Timeline

- 2022-09-30 - Vulnerability reported to vendor
- 2022-12-15 - Coordinated public release of advisory
