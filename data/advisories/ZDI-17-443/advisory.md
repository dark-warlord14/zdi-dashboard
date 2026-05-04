# ZDI-17-443: Cisco WebEx Network Recording Player ARF File Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-443
- **ZDI-CAN:** ZDI-CAN-4278
- **Date:** 2017-06-23
- **CVE:** CVE-2017-6669
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Cisco
- **Affected Products:** WebEx
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-443/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Cisco WebEx Network Recording Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of ARF files. The issue results from the lack of proper validation of user-supplied data which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-20170621-wnrp

## Disclosure Timeline

- 2016-12-19 - Vulnerability reported to vendor
- 2017-06-23 - Coordinated public release of advisory
