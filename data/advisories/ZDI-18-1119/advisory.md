# ZDI-18-1119: Cisco WebEx Network Recording Player ATPDMOD ARF File Heap-based Buffer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1119
- **ZDI-CAN:** ZDI-CAN-6311
- **Date:** 2018-10-08
- **CVE:** CVE-2018-15409
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Cisco
- **Affected Products:** WebEx
- **Credit:** Steven Seeley (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1119/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Cisco WebEx Network Recording Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of ARF files. Crafted data in a ARF file can trigger an overflow of a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20181003-webex-rce

## Disclosure Timeline

- 2018-06-06 - Vulnerability reported to vendor
- 2018-10-08 - Coordinated public release of advisory
- 2018-10-08 - Advisory Updated
