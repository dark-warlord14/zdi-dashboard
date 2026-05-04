# ZDI-17-936: Cisco WebEx Recorder and Player WRF File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-936
- **ZDI-CAN:** ZDI-CAN-4988
- **Date:** 2017-12-06
- **CVE:** CVE-2017-12370
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Cisco
- **Affected Products:** WebEx
- **Credit:** Steven Seeley (mr_me) of Offensive Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-936/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Cisco WebEx Recorder and Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of WRF files. Crafted data in a WRF file can trigger an overflow of a heap-based buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20171129-webex-players

## Disclosure Timeline

- 2017-07-25 - Vulnerability reported to vendor
- 2017-12-06 - Coordinated public release of advisory
