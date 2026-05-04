# ZDI-13-073: Oracle Java setICMpixels Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-073
- **ZDI-CAN:** ZDI-CAN-1716
- **Date:** 2013-05-10
- **CVE:** CVE-2013-2420
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Vitaliy Toropov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-073/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the sun.awt.image.ImageRepresentation.setICMpixels' native function. The issue lies in the handling of the scanlineStride argument, which is not properly validated before being used. By manipulating the function's arguments an attacker can force an integer overflow to occur before indexing into an array. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpuapr2013-1928497.html

## Disclosure Timeline

- 2013-02-01 - Vulnerability reported to vendor
- 2013-05-10 - Coordinated public release of advisory
