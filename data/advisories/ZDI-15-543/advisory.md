# ZDI-15-543: Microsoft Office Excel Binary Worksheet Uninitialized Pointer Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-543
- **ZDI-CAN:** ZDI-CAN-3109
- **Date:** 2015-11-10
- **CVE:** CVE-2015-6038
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Excel
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-543/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Office Excel. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of binary (.xlsb) Excel files. By providing a malformed .xlsb file, an attacker can cause the target location for a branch to be read from uninitialized memory. An attacker could leverage this to execute arbitrary code under the context of the Excel process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-116

## Disclosure Timeline

- 2015-08-03 - Vulnerability reported to vendor
- 2015-11-10 - Coordinated public release of advisory
