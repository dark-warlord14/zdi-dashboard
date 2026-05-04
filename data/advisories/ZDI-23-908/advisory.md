# ZDI-23-908: Dassault Systèmes SolidWorks DXF File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-908
- **ZDI-CAN:** ZDI-CAN-20882
- **Date:** 2023-07-12
- **CVE:** CVE-2023-2763
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Dassault Systèmes
- **Affected Products:** SolidWorks
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-908/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Dassault Syst��mes SolidWorks. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DXF files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

https://www.cve.org/CVERecord?id=CVE-2023-2763 https://www.3ds.com/vulnerability/advisories

## Disclosure Timeline

- 2023-04-13 - Vulnerability reported to vendor
- 2023-07-12 - Coordinated public release of advisory
- 2023-09-20 - Advisory Updated
