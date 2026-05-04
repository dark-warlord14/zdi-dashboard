# ZDI-18-007: Cisco WebEx ARF File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-007
- **ZDI-CAN:** ZDI-CAN-4913
- **Date:** 2018-01-03
- **CVE:** CVE-2018-0103
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Cisco
- **Affected Products:** WebEx
- **Credit:** Steven Seeley (mr_me) of Offensive Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-007/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Cisco WebEx Network Recording Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of ARF files. Crafted data in an ARF file can trigger an overflow of a heap-based buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20180103-wnrp

## Disclosure Timeline

- 2017-07-19 - Vulnerability reported to vendor
- 2018-01-03 - Coordinated public release of advisory
