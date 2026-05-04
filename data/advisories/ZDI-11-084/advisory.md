# ZDI-11-084: Oracle Java Unsigned Applet Applet2ClassLoader Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-084
- **ZDI-CAN:** ZDI-CAN-926
- **Date:** 2011-02-15
- **CVE:** CVE-2010-4452
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Frederic Hoguin
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-084/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the Java Runtime Environment. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the findClass method of the sun.plugin2.applet.Applet2ClassLoader class. Due to a failure to properly validate URLs supplied by an implicitly trusted applet, it is possible to execute arbitrary code on Windows 32-bit and 64-bit, as well as Linux 32-bit platforms under the context of the SYSTEM user.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpufeb2011-304611.html

## Disclosure Timeline

- 2010-09-28 - Vulnerability reported to vendor
- 2011-02-15 - Coordinated public release of advisory
