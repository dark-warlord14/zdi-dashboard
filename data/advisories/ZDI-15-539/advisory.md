# ZDI-15-539: Microsoft Office Word TTF Size Miscalculation Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-539
- **ZDI-CAN:** ZDI-CAN-3102
- **Date:** 2015-11-10
- **CVE:** CVE-2015-6093
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Word
- **Credit:** SignalSEC Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-539/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office Word. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of name tables in an embedded TTF file. Incorrect processing of a size value can cause Word to copy too much data and corrupt memory. An attacker could leverage this vulnerability to execute arbitrary code in the context of the process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-116

## Disclosure Timeline

- 2015-07-28 - Vulnerability reported to vendor
- 2015-11-10 - Coordinated public release of advisory
