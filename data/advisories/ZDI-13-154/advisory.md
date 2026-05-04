# ZDI-13-154: Oracle Java ByteComponentRaster Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-154
- **ZDI-CAN:** ZDI-CAN-1831
- **Date:** 2013-06-27
- **CVE:** CVE-2013-2473
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Vitaliy Toropov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-154/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the java.awt.image.ByteComponentRaster class. The issue lies in the failure to properly verify that a buffer is large enough prior to copying data into it. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpujun2013-1899847.html

## Disclosure Timeline

- 2013-03-29 - Vulnerability reported to vendor
- 2013-06-27 - Coordinated public release of advisory
