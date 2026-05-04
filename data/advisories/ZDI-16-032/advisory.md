# ZDI-16-032: Oracle Java readImage Heap Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-032
- **ZDI-CAN:** ZDI-CAN-3282
- **Date:** 2016-01-25
- **CVE:** CVE-2016-0483
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-032/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of image data. The issue lies in insufficient validation of supplied image data inside the native function readImage. An attacker can leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpujan2016-2367955.html

## Disclosure Timeline

- 2015-10-01 - Vulnerability reported to vendor
- 2016-01-25 - Coordinated public release of advisory
