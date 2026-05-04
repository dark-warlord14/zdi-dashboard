# ZDI-17-452: (0Day) Advantech WebOP Designer Project File Heap Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-452
- **ZDI-CAN:** ZDI-CAN-3703
- **Date:** 2017-08-15
- **CVE:** CVE-2017-12705
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Advantech
- **Affected Products:** WebOP Designer
- **Credit:** Ariele Caltabiano (kimiya)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-452/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Advantech WebOP Designer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of a pm3 project file. A heap-based buffer overflow vulnerability exists in a call to memcpy. An attacker can leverage this vulnerability to execute arbitrary code in the context of the process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 04/27/16 - ZDI disclosed the vulnerability report to US ICS-CERT 04/27/16 - US ICS-CERT acknowledged and provided ICS-VU# 148103 05/11/16 - US ICS-CERT requested further details to reproduce the report 05/11/16 - ZDI provided updated materials 10/12/16 - ZDI requested a status update 10/12/16 - US ICS-CERT agreed to follow up the next week 03/01/17 - US ICS-CERT wrote to say that the vendor still cannot reproduce the report 03/15/17 - US ICS-CERT wrote to say that the vendor still cannot reproduce the report and requested assistance 04/04/17 - US ICS-CERT wrote to say that the vendor still cannot reproduce the report and requested assistance 04/05/17 - ZDI provided detailed steps for reproducing the report 06/02/17 - ZDI requested a status update 06/22/17 - ZDI requested a status update -- Mitigation: Given the stated purpose of Advantech WebOP Designer, and the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application to trusted files.

## Disclosure Timeline

- 2016-04-27 - Vulnerability reported to vendor
- 2017-08-15 - Coordinated public release of advisory
