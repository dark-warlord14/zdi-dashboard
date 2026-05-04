# ZDI-10-061: Sun Java Runtime CMM readMabCurveData Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-061
- **ZDI-CAN:** ZDI-CAN-625
- **Date:** 2010-04-05
- **CVE:** CVE-2010-0838
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Sun Microsystems
- **Affected Products:** Java Runtime
- **Credit:** Stephen Fewer of Harmony Security (www.harmonysecurity.com)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-061/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Sun's Java Runtime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists within the CMM module of the Sun JVM. This module contains a function readMabCurveData. An applet can indirectly call this function and provide it with a malicious curv object. The function trusts the size of the curv element implicitly and copies the data into a fixed-length stack buffer. Exploitation of this issue can lead to arbitrary code execution under the context of the user invoking the applet.

## Additional Details

Sun Microsystems has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technology/deploy/security/critical-patch-updates/javacpumar2010.html

## Disclosure Timeline

- 2009-11-09 - Vulnerability reported to vendor
- 2010-04-05 - Coordinated public release of advisory
