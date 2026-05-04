# ZDI-18-968: Cisco WebEx Network Recording Player ARF File Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-968
- **ZDI-CAN:** ZDI-CAN-5600
- **Date:** 2018-08-31
- **CVE:** CVE-2018-0379
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Cisco
- **Affected Products:** WebEx
- **Credit:** b0nd @garage4hackers
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-968/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Cisco WebEx Network Recording Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of ARF files. Crafted data can trigger an overflow of a heap-based buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20180718-webex-rce

## Disclosure Timeline

- 2018-04-04 - Vulnerability reported to vendor
- 2018-08-31 - Coordinated public release of advisory
- 2018-08-31 - Advisory Updated
