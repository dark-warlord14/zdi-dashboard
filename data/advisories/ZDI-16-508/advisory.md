# ZDI-16-508: Microsoft Office Excel Art Data Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-508
- **ZDI-CAN:** ZDI-CAN-3781
- **Date:** 2016-09-16
- **CVE:** CVE-2016-3365
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Excel
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-508/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office Excel. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of art data within a spreadsheet. The issue lies in the failure to properly validate user-supplied data which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS16-107

## Disclosure Timeline

- 2016-06-06 - Vulnerability reported to vendor
- 2016-09-16 - Coordinated public release of advisory
