# ZDI-15-516: Microsoft Office Excel fileVersion Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-516
- **ZDI-CAN:** ZDI-CAN-3038
- **Date:** 2015-10-13
- **CVE:** CVE-2015-2558
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Excel
- **Credit:** 3S Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-516/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office Excel. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of the fileVersion element in the workbook. By providing an overly long value, an attacker can force an object to be used after it has been freed. This could allow the attacker to execute arbitrary code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/MS15-110

## Disclosure Timeline

- 2015-07-02 - Vulnerability reported to vendor
- 2015-10-13 - Coordinated public release of advisory
