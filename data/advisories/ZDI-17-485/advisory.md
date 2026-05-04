# ZDI-17-485: Fuji Electric V-Server VPR File Parsing Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-485
- **ZDI-CAN:** ZDI-CAN-4030
- **Date:** 2017-07-12
- **CVE:** CVE-2017-9639
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Fuji Electric
- **Affected Products:** V-Server
- **Credit:** Ariele Caltabiano (kimiya)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-485/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Fuji Electric V-Server. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within parsing of a VPR file. The issue results from the lack of proper validation of user-supplied data which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Fuji Electric has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-17-192-02

## Disclosure Timeline

- 2016-09-27 - Vulnerability reported to vendor
- 2017-07-12 - Coordinated public release of advisory
