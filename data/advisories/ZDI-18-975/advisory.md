# ZDI-18-975: Cisco WebEx Network Recording Player NBRQA Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-975
- **ZDI-CAN:** ZDI-CAN-5721
- **Date:** 2018-08-31
- **CVE:** CVE-2018-0379
- **CVSS:** 5.1
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Cisco
- **Affected Products:** WebEx
- **Credit:** Steven Seeley (mr_me) of Offensive Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-975/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Cisco WebEx Network Recording Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the NBRQA.DLL module. Crafted data in an ARF file can trigger an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20180718-webex-rce

## Disclosure Timeline

- 2018-03-23 - Vulnerability reported to vendor
- 2018-08-31 - Coordinated public release of advisory
- 2018-08-31 - Advisory Updated
