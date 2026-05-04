# ZDI-15-326: Microsoft Office Excel pivotField Heap Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-326
- **ZDI-CAN:** ZDI-CAN-2896
- **Date:** 2015-07-14
- **CVE:** CVE-2015-2376
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Excel
- **Credit:** 3S Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-326/
## Vulnerability Details

This vulnerability allows remote attackers to corrupt heap memory on vulnerable installations of Microsoft Office Excel. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within processing of pivotField objects. A specially crafted spreadsheet can cause Excel to write information past the end of a heap-allocated buffer. An attacker may be able to leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/MS15-070

## Disclosure Timeline

- 2015-04-23 - Vulnerability reported to vendor
- 2015-07-14 - Coordinated public release of advisory
