# ZDI-20-1224: Trend Micro OfficeScan ServerMigrationTool DAT File Parsing Double Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1224
- **ZDI-CAN:** ZDI-CAN-10973
- **Date:** 2020-09-25
- **CVE:** CVE-2020-25773
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trend Micro
- **Affected Products:** OfficeScan
- **Credit:** Jaehun Jeong(@n3sk) of Theori
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1224/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Trend Micro OfficeScan ServerMigrationTool. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of DAT files. The issue results from the lack of validating the existence of an object prior to performing further free operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/000271974

## Disclosure Timeline

- 2020-05-21 - Vulnerability reported to vendor
- 2020-09-25 - Coordinated public release of advisory
